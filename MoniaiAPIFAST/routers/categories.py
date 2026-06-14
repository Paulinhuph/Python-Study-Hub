
import logging
from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from MoniaiAPIFAST.database import get_authed_client
from MoniaiAPIFAST.core.dependencies import get_user_id
from MoniaiAPIFAST.schemas.category import CategoryCreate, CategoryUpdate

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/categories", tags=["Categories"])
security = HTTPBearer()


#  GET /categories  —  Listar categorias do usuário
@router.get("/", status_code=200)
async def get_categories(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    token = credentials.credentials
    get_user_id(token)
    db = get_authed_client(token)

    try:
        response = db.table("categories").select("*").order(
            "is_default", desc=True
        ).order("nome").execute()

        return {
            "message": "Categorias recuperadas com sucesso!",
            "count": len(response.data),
            "data": response.data,
        }

    except Exception as e:
        logger.exception("Erro ao buscar categorias")
        raise HTTPException(status_code=500, detail="Erro ao buscar categorias.")


#  POST /categories  —  Criar categoria
@router.post("/", status_code=201)
async def create_category(
    category_data: CategoryCreate,
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    token = credentials.credentials
    user_id = get_user_id(token)
    db = get_authed_client(token)

    try:
        response = db.table("categories").insert({
            "user_id": user_id,
            "nome":    category_data.nome,
            "icone":   category_data.icone,
            "cor":     category_data.cor,
        }).execute()

        return {
            "message": "Categoria criada com sucesso!",
            "data": response.data,
        }

    except Exception as e:
        error_msg = str(e)
        if "duplicate" in error_msg.lower() or "unique" in error_msg.lower():
            raise HTTPException(status_code=400, detail="Você já possui uma categoria com esse nome.")
        logger.exception("Erro ao criar categoria")
        raise HTTPException(status_code=500, detail="Erro interno ao criar categoria.")


#  PUT /categories/{id}  —  Editar categoria
@router.put("/{id}", status_code=200)
async def update_category(
    id: str,
    category_data: CategoryUpdate,
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    token = credentials.credentials
    get_user_id(token)
    db = get_authed_client(token)

    try:
        # Monta apenas os campos que foram enviados
        campos = {k: v for k, v in category_data.model_dump().items() if v is not None}

        if not campos:
            raise HTTPException(status_code=400, detail="Nenhum campo enviado para atualização.")

        response = db.table("categories").update(campos).eq("id", id).execute()

        if not response.data:
            raise HTTPException(
                status_code=404,
                detail="Categoria não encontrada ou sem permissão para editar.",
            )

        return {
            "message": "Categoria atualizada com sucesso!",
            "data": response.data,
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.exception("Erro ao atualizar categoria")
        raise HTTPException(status_code=500, detail="Erro interno ao atualizar categoria.")



#  DELETE /categories/{id}  —  Excluir categoria
#  Bloqueado se existirem transações vinculadas
@router.delete("/{id}", status_code=200)
async def delete_category(
    id: str,
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    token = credentials.credentials
    get_user_id(token)
    db = get_authed_client(token)

    try:
        # Apaga todas as transações vinculadas primeiro (Cascade)
        db.table("transactions").delete().eq("categoria_id", id).execute()

        response = db.table("categories").delete().eq("id", id).execute()

        if not response.data:
            raise HTTPException(
                status_code=404,
                detail="Categoria não encontrada ou sem permissão para excluí-la.",
            )

        return {
            "message": "Categoria excluída com sucesso!",
            "id_deletado": id,
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.exception("Erro ao excluir categoria")
        raise HTTPException(status_code=500, detail="Erro interno ao excluir categoria.")


#  POST /categories/seed  —  Popular categorias padrão
#  Chama a função SQL seed_default_categories do Supabase
@router.post("/seed", status_code=201)
async def seed_categories(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    token = credentials.credentials
    user_id = get_user_id(token)
    db = get_authed_client(token)

    try:
        # Verifica se o usuário já tem categorias
        existing = db.table("categories").select("id").limit(1).execute()

        if existing.data:
            raise HTTPException(
                status_code=400,
                detail="Você já possui categorias cadastradas.",
            )

        # Chama a função SQL que criamos no Supabase
        db.rpc("seed_default_categories", {"p_user_id": user_id}).execute()

        return {"message": "Categorias padrão criadas com sucesso!"}

    except HTTPException:
        raise
    except Exception as e:
        logger.exception("Erro ao criar categorias padrão")
        raise HTTPException(status_code=500, detail="Erro ao criar categorias padrão.")