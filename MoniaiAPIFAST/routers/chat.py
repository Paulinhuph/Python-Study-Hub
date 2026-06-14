





import json
import logging
from datetime import date
from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import StreamingResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from MoniaiAPIFAST.database import get_authed_client
from MoniaiAPIFAST.core.dependencies import get_user_id
from MoniaiAPIFAST.core.config import settings
from MoniaiAPIFAST.schemas.chat_schemas import ChatMessage
from groq import Groq

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/chat", tags=["Chat"])
security = HTTPBearer()


#  Helper: monta o system prompt com dados reais do usuário
def build_system_prompt(db, user_id: str) -> str:
    try:
        mes_ref = date.today().strftime("%Y-%m")

        import calendar
        try:
            y, m = map(int, mes_ref.split('-'))
            ultimo_dia = calendar.monthrange(y, m)[1]
        except:
            ultimo_dia = 31

        # Busca resumo financeiro do mês atual
        tx = db.table("transactions").select("tipo, valor, categories(nome)").gte(
            "data", f"{mes_ref}-01"
        ).lte("data", f"{mes_ref}-{ultimo_dia}").execute()

        receitas  = sum(t["valor"] for t in tx.data if t["tipo"] == "receita")
        despesas  = sum(t["valor"] for t in tx.data if t["tipo"] == "despesa")
        saldo     = receitas - despesas
        economia  = round((saldo / receitas * 100), 1) if receitas > 0 else 0.0

        # Agrupa top gastos por categoria
        cat_totais: dict = {}
        for t in tx.data:
            if t["tipo"] == "despesa":
                cat = t.get("categories") or {}
                nome = cat.get("nome", "Sem categoria")
                cat_totais[nome] = cat_totais.get(nome, 0) + t["valor"]

        top_cats = sorted(cat_totais.items(), key=lambda x: x[1], reverse=True)[:3]
        top_str  = ", ".join(f"{c}: R$ {v:.2f}" for c, v in top_cats) or "nenhum gasto registrado"

        contexto = f"""Dados financeiros do usuário em {mes_ref}:
- Receitas: R$ {receitas:.2f}
- Despesas: R$ {despesas:.2f}
- Saldo: R$ {saldo:.2f}
- Taxa de economia: {economia}%
- Top gastos: {top_str}"""

    except Exception:
        contexto = "Dados financeiros não disponíveis no momento."

    return f"""Você é o Monety, um assistente financeiro pessoal inteligente, direto e amigável.
Responda sempre em português do Brasil. Use formatação simples com **negrito** quando necessário.
Seja objetivo — máximo 4 parágrafos por resposta.
Baseie suas análises nos dados reais do usuário abaixo.
Não invente dados que não estejam no contexto.
Você não é um consultor financeiro profissional — deixe isso claro quando necessário.

{contexto}"""


#
#  POST /chat/message  —  Enviar mensagem (streaming SSE)
@router.post("/message", status_code=200)
async def send_message(
    body: ChatMessage,
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    token    = credentials.credentials
    user_id  = get_user_id(token)
    db       = get_authed_client(token)

    if not settings.GROQ_API_KEY:
        raise HTTPException(status_code=500, detail="GROQ_API_KEY não configurada.")

    # Busca últimas 20 mensagens do histórico
    try:
        hist = db.table("chat_history").select("role, content").eq(
            "user_id", user_id
        ).order("created_at", desc=True).limit(20).execute()

        historico = [{"role": m["role"], "content": m["content"]}
                     for m in reversed(hist.data) if m.get("content") and str(m.get("content")).strip()]
    except Exception:
        historico = []

    system_prompt = build_system_prompt(db, user_id)

    mensagens = [
        {"role": "system", "content": system_prompt},
        *historico,
        {"role": "user", "content": body.message},
    ]

    # Salva mensagem do usuário no banco
    try:
        db.table("chat_history").insert({
            "user_id": user_id,
            "role":    "user",
            "content": body.message,
        }).execute()
    except Exception:
        pass  # não bloqueia o fluxo se falhar

    # Streaming SSE com Groq
    async def stream_groq():
        client   = Groq(api_key=settings.GROQ_API_KEY)
        resposta = ""

        try:
            stream = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=mensagens,
                max_tokens=1024,
                temperature=0.7,
                stream=True,
            )

            for chunk in stream:
                delta = chunk.choices[0].delta.content or ""
                if delta:
                    resposta += delta
                    yield f"data: {json.dumps({'token': delta})}\n\n"

            # Salva resposta completa da IA no histórico
            try:
                db.table("chat_history").insert({
                    "user_id": user_id,
                    "role":    "assistant",
                    "content": resposta,
                }).execute()
            except Exception:
                pass

            yield f"data: {json.dumps({'done': True})}\n\n"

        except Exception as e:
            logger.exception("Erro no streaming Groq")
            yield f"data: {json.dumps({'error': 'Erro ao gerar resposta da IA.'})}\n\n"

    return StreamingResponse(
        stream_groq(),
        media_type="text/event-stream",
        headers={
            "Cache-Control":               "no-cache",
            "X-Accel-Buffering":           "no",
            "Access-Control-Allow-Origin": "*",
        },
    )



#  GET /chat/history  —  Buscar histórico de mensagens
@router.get("/history", status_code=200)
async def get_history(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    limite: int = 50,
):
    token   = credentials.credentials
    user_id = get_user_id(token)
    db      = get_authed_client(token)

    try:
        response = db.table("chat_history").select(
            "id, role, content, created_at"
        ).eq("user_id", user_id).order(
            "created_at", desc=False
        ).limit(limite).execute()

        return {
            "message": "Histórico recuperado com sucesso!",
            "count":   len(response.data),
            "data":    response.data,
        }

    except Exception as e:
        logger.exception("Erro ao buscar histórico")
        raise HTTPException(status_code=500, detail="Erro ao buscar histórico.")


#  DELETE /chat/history  —  Limpar histórico do usuário
@router.delete("/history", status_code=200)
async def clear_history(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    token   = credentials.credentials
    user_id = get_user_id(token)
    db      = get_authed_client(token)

    try:
        db.table("chat_history").delete().eq("user_id", user_id).execute()

        return {"message": "Histórico limpo com sucesso!"}

    except Exception as e:
        logger.exception("Erro ao limpar histórico")
        raise HTTPException(status_code=500, detail="Erro ao limpar histórico.")