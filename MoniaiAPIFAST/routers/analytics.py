import calendar
import logging
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from MoniaiAPIFAST.database import get_authed_client
from MoniaiAPIFAST.core.dependencies import get_user_id

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/analytics", tags=["Analytics"])
security = HTTPBearer()

#  GET /analytics/balance  —  Saldo, receitas e despesas

@router.get("/balance", status_code=200)
async def get_balance(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    mes: str | None = None,
):
    token = credentials.credentials
    user_id = get_user_id(token)  # 🎯 O ID é validado localmente e capturado
    db = get_authed_client(token)

    try:
        from datetime import date
        mes_ref = mes or date.today().strftime("%Y-%m")
        
        # 1. Separa o ano e o mês para calcular o último dia
        try:
            y, m = map(int, mes_ref.split('-'))
            ultimo_dia = calendar.monthrange(y, m)[1]
        except:
            ultimo_dia = 31

        # 2. Constrói a query usando o último dia calculado dinamicamente
        query = db.table("transactions").select("valor, tipo").gte(
            "data", f"{mes_ref}-01"
        ).lte("data", f"{mes_ref}-{ultimo_dia}") # ← Aqui o '-31' morre
        
        query = query.eq("user_id", user_id)
        response = query.execute()

        total_receitas = 0.0
        total_despesas = 0.0

        for item in response.data:
            if item["tipo"] == "receita":
                total_receitas += item["valor"]
            elif item["tipo"] == "despesa":
                total_despesas += item["valor"]

        saldo    = total_receitas - total_despesas
        economia = round((saldo / total_receitas * 100), 2) if total_receitas > 0 else 0.0

        return {
            "mes":            mes_ref,
            "saldo_atual":    round(saldo, 2),
            "total_receitas": round(total_receitas, 2),
            "total_despesas": round(total_despesas, 2),
            "economia_pct":   economia,
        }

    except Exception as e:
        error_msg = str(e)
        if "JWT" in error_msg or "token" in error_msg.lower() or "401" in error_msg:
            raise HTTPException(status_code=401, detail="Token inválido ou expirado.")
        logger.exception("Erro no analytics/balance")
        raise HTTPException(status_code=500, detail="Erro interno no analytics.")

#  GET /analytics/by-category  —  Gastos agrupados por categoria
@router.get("/by-category", status_code=200)
async def get_by_category(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    mes: str | None = None,
):
    token = credentials.credentials
    user_id = get_user_id(token) # 🎯 O ID é capturado novamente
    db = get_authed_client(token)

    try:
        from datetime import date
        mes_ref = mes or date.today().strftime("%Y-%m")

        try:
            y, m = map(int, mes_ref.split('-'))
            ultimo_dia = calendar.monthrange(y, m)[1]
        except:
            ultimo_dia = 31

        query = db.table("transactions").select(
            "valor, tipo, categories(nome, icone, cor)"
        ).eq("tipo", "despesa").gte(
            "data", f"{mes_ref}-01"
        ).lte("data", f"{mes_ref}-{ultimo_dia}")
        
        # 🛡️ DEFESA EM PROFUNDIDADE APLICADA AQUI TAMBÉM
        query = query.eq("user_id", user_id)
        
        response = query.execute()

        agrupado: dict = {}
        for item in response.data:
            cat = item.get("categories") or {}
            nome = cat.get("nome", "Sem categoria")
            if nome not in agrupado:
                agrupado[nome] = {
                    "nome":  nome,
                    "icone": cat.get("icone", "📦"),
                    "cor":   cat.get("cor", "#888"),
                    "total": 0.0,
                }
            agrupado[nome]["total"] += item["valor"]

        resultado = sorted(
            [{"nome": v["nome"], "icone": v["icone"], "cor": v["cor"], "total": round(v["total"], 2)}
             for v in agrupado.values()],
            key=lambda x: x["total"],
            reverse=True,
        )

        total_geral = sum(r["total"] for r in resultado)

        for r in resultado:
            r["percentual"] = round((r["total"] / total_geral * 100), 1) if total_geral > 0 else 0.0

        return {
            "mes":           mes_ref,
            "total_despesas": round(total_geral, 2),
            "categorias":    resultado,
        }

    except Exception as e:
        logger.exception("Erro no analytics/by-category")
        raise HTTPException(status_code=500, detail="Erro ao agrupar por categoria.")