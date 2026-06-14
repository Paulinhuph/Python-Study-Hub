




import calendar
import logging
from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from MoniaiAPIFAST.schemas.transaction import TransactionCreate
from MoniaiAPIFAST.database import get_authed_client
from MoniaiAPIFAST.core.dependencies import get_user_id

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/transactions", tags=["Transactions"])
security = HTTPBearer()


#  POST /transactions  —  Criar transação

@router.post("/", status_code=201)
async def create_transaction(
    transaction_data: TransactionCreate,
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    token = credentials.credentials
    user_id = get_user_id(token)
    db = get_authed_client(token)

    try:
        response = db.table("transactions").insert({
            "user_id":      user_id,
            "descricao":    transaction_data.descricao,
            "valor":        transaction_data.valor,
            "tipo":         transaction_data.tipo,
            "categoria_id": str(transaction_data.categoria_id),
            "data":         str(transaction_data.data),
        }).execute()

        return {
            "message": "Transação registrada com sucesso!",
            "data": response.data,
        }

    except Exception as e:
        error_msg = str(e)
        if "violates foreign key" in error_msg:
            raise HTTPException(status_code=400, detail="Categoria não encontrada.")
        logger.exception("Erro ao criar transação")
        raise HTTPException(status_code=500, detail="Erro interno ao criar transação.")


#  GET /transactions  —  Listar com paginação e filtros
@router.get("/", status_code=200)
async def get_transactions(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    pagina: int = 1,
    tipo: str | None = None,
    categoria_id: str | None = None,
    mes: str | None = None,
):
    token = credentials.credentials
    get_user_id(token)
    db = get_authed_client(token)

    try:
        tamanho_pagina = 15
        inicio = (pagina - 1) * tamanho_pagina
        fim = inicio + tamanho_pagina - 1

        query = db.table("transactions").select(
            "*, categories(nome, icone, cor)"
        ).order("data", desc=True)

        if tipo:
            query = query.eq("tipo", tipo)
        if categoria_id:
            query = query.eq("categoria_id", categoria_id)
        if mes:
            try:
                y, m = map(int, mes.split('-'))
                ultimo_dia = calendar.monthrange(y, m)[1]
                query = query.gte("data", f"{mes}-01").lte("data", f"{mes}-{ultimo_dia}")
            except Exception:
                query = query.gte("data", f"{mes}-01").lte("data", f"{mes}-31")

        response = query.range(inicio, fim).execute()

        return {
            "message": "Transações recuperadas com sucesso!",
            "pagina_atual": pagina,
            "count": len(response.data),
            "data": response.data,
        }

    except Exception as e:
        logger.exception("Erro ao buscar transações")
        raise HTTPException(status_code=500, detail="Erro ao buscar transações.")


#  GET /transactions/summary  —  Totais do mês para o dashboard
@router.get("/summary", status_code=200)
async def get_summary(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    mes: str | None = None,
):
    token = credentials.credentials
    get_user_id(token)
    db = get_authed_client(token)

    try:
        from datetime import date
        mes_ref = mes or date.today().strftime("%Y-%m")
        y, m = map(int, mes_ref.split('-'))
        ultimo_dia = calendar.monthrange(y, m)[1]

        response = db.table("transactions").select("tipo, valor").gte(
            "data", f"{mes_ref}-01"
        ).lte("data", f"{mes_ref}-{ultimo_dia}").execute()

        receitas = sum(t["valor"] for t in response.data if t["tipo"] == "receita")
        despesas = sum(t["valor"] for t in response.data if t["tipo"] == "despesa")
        saldo    = receitas - despesas
        economia = round((saldo / receitas * 100), 2) if receitas > 0 else 0.0

        return {
            "mes":          mes_ref,
            "receitas":     round(receitas, 2),
            "despesas":     round(despesas, 2),
            "saldo":        round(saldo, 2),
            "economia_pct": economia,
        }

    except Exception as e:
        logger.exception("Erro ao calcular resumo")
        raise HTTPException(status_code=500, detail="Erro ao calcular resumo.")


#  PUT /transactions/{id}  —  Editar transação
@router.put("/{id}", status_code=200)
async def update_transaction(
    id: str,
    transaction_data: TransactionCreate,
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    token = credentials.credentials
    get_user_id(token)
    db = get_authed_client(token)

    try:
        response = db.table("transactions").update({
            "descricao":    transaction_data.descricao,
            "valor":        transaction_data.valor,
            "tipo":         transaction_data.tipo,
            "categoria_id": str(transaction_data.categoria_id),
            "data":         str(transaction_data.data),
        }).eq("id", id).execute()

        if not response.data:
            raise HTTPException(
                status_code=404,
                detail="Transação não encontrada ou sem permissão para editar.",
            )

        return {
            "message": "Transação atualizada com sucesso!",
            "data": response.data,
        }

    except HTTPException:
        raise
    except Exception as e:
        error_msg = str(e)
        if "violates foreign key" in error_msg:
            raise HTTPException(status_code=400, detail="Categoria não encontrada.")
        logger.exception("Erro ao atualizar transação")
        raise HTTPException(status_code=500, detail="Erro interno ao atualizar transação.")


# ──────────────────────────────────────────────────────────────
#  DELETE /transactions/{id}  —  Excluir transação
# ──────────────────────────────────────────────────────────────
@router.delete("/{id}", status_code=200)
async def delete_transaction(
    id: str,
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    token = credentials.credentials
    get_user_id(token)
    db = get_authed_client(token)

    try:
        response = db.table("transactions").delete().eq("id", id).execute()

        if not response.data:
            raise HTTPException(
                status_code=404,
                detail="Transação não encontrada ou sem permissão para excluí-la.",
            )

        return {
            "message": "Transação deletada com sucesso!",
            "id_deletado": id,
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.exception("Erro ao excluir transação")
        raise HTTPException(status_code=500, detail="Erro interno ao excluir transação.")