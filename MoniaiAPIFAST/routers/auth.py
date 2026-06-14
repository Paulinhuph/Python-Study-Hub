import logging
from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from MoniaiAPIFAST.schemas.auth import UserRegister, UserLogin, UserUpdate, PasswordUpdate, AvatarUpdate
from MoniaiAPIFAST.database import supabase, get_authed_client
from MoniaiAPIFAST.core.dependencies import get_user_id
from gotrue.errors import AuthApiError

logger = logging.getLogger(__name__)

security = HTTPBearer()

router = APIRouter(prefix="/auth", tags=["Authentication"])

# --- ROTA DE CADASTRO ---
@router.post("/register", status_code=201)
async def register(user_data: UserRegister):  
    try: # Faz a chamada ao módulo de Autenticação do Supabase
        response = supabase.auth.sign_up({
            "email": user_data.email,
            "password": user_data.password,
            "options": {
                # Enviamos o nome dentro de 'data' para que a Trigger SQL 
                # consiga ler e espelhar na tabela 'profiles' 
                "data": {
                    "nome": user_data.nome
                }
            }
        })
        # Se tudo der certo, retorna os dados básicos do usuário criado
        return {
            "message": "Usuário criado com sucesso!",
            "user_id": response.user.id,
            "email": response.user.email            
        }
    
    except AuthApiError as auth_err:
        # Captura erros de regra de negócio do Supabase (ex: e-mail já cadastrado)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Erro na autenticação do Supabase: {auth_err.message}"
        )
    except Exception as e:
        logger.exception("Erro inesperado no registro")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro interno no servidor."
        )

# --- ROTA DE LOGIN ---
@router.post("/login", status_code=200)
async def login(user_data: UserLogin):
    try:
        response = supabase.auth.sign_in_with_password({
            "email": user_data.email,
            "password": user_data.password
        })
        user_id = response.user.id
        email = response.user.email
        
        # Busca o perfil do usuário para retornar nome e avatar
        nome = "Usuário"
        avatar_url = None
        try:
            # Precisamos usar a chave de serviço ou a anon key com o token retornado
            client = get_authed_client(response.session.access_token)
            prof = client.table("profiles").select("nome, avatar_url").eq("id", user_id).execute()
            if prof.data:
                nome = prof.data[0].get("nome", "Usuário")
                avatar_url = prof.data[0].get("avatar_url")
        except Exception:
            pass

        return {
            "message": "Login realizado com sucesso!",
            "access_token": response.session.access_token,
            "token_type": "bearer",
            "user": {
                "id": user_id,
                "email": email,
                "nome": nome,
                "avatar_url": avatar_url
            }
        }
    except AuthApiError as auth_err:
            # Captura erros diretos de autenticação do Supabase
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="E-mail ou senha incorretos."
            )
    except Exception as e:
        # Se o Supabase mandou uma string de credenciais inválidas, tratamos como 401
        if "Invalid login credentials" in str(e):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="E-mail ou senha incorretos."
            )
            
        logger.exception("Erro inesperado no login")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro interno no servidor."
        )
    
# --- ROTA DE ATUALIZAÇÃO DE PERFIL ---
@router.put("/profile", status_code=200)
async def update_profile(
    user_data: UserUpdate,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials
    user_id = get_user_id(token)
    db = get_authed_client(token)

    try:
        # Tenta atualizar o nome na tabela profiles vinculada ao id do usuario
        response = db.table("profiles").update({"nome": user_data.nome}).eq("id", user_id).execute()
        
        return {
            "message": "Perfil atualizado com sucesso no backend!",
            "nome": user_data.nome,
            "email": user_data.email
        }
    except Exception as e:
        logger.exception("Erro ao atualizar perfil")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro ao atualizar perfil."
        )

# --- ROTA DE ATUALIZAÇÃO DE SENHA ---
@router.put("/password", status_code=200)
async def update_password(
    data: PasswordUpdate,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials
    # A autenticação já está validada via JWT, mas precisamos do email
    try:
        user_res = supabase.auth.get_user(token)
        email = user_res.user.email
    except Exception:
        raise HTTPException(status_code=401, detail="Token inválido.")

    # Verifica a senha atual
    try:
        supabase.auth.sign_in_with_password({"email": email, "password": data.senha_atual})
    except Exception:
        raise HTTPException(status_code=401, detail="Senha atual incorreta.")

    # Atualiza para a nova senha
    try:
        # update_user requer a sessão ativa, mas no Supabase python podemos usar o serviço admin
        # ou atualizar pelo cliente autenticado. Como supabase global não guarda sessão, 
        # a melhor forma é usar a API de Admin (Service Role)
        from MoniaiAPIFAST.core.config import settings
        from supabase import create_client
        service_client = create_client(settings.SUPABASE_URL, settings.SUPABASE_SERVICE_ROLE_KEY)
        
        service_client.auth.admin.update_user_by_id(user_res.user.id, {"password": data.nova_senha})
        return {"message": "Senha atualizada com sucesso!"}
    except Exception as e:
        logger.exception("Erro ao atualizar senha")
        raise HTTPException(status_code=500, detail="Erro ao atualizar senha.")

# --- ROTA DE EXCLUSÃO DE CONTA ---
@router.delete("/account", status_code=200)
async def delete_account(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials
    user_id = get_user_id(token)

    try:
        from MoniaiAPIFAST.core.config import settings
        from supabase import create_client
        service_client = create_client(settings.SUPABASE_URL, settings.SUPABASE_SERVICE_ROLE_KEY)
        
        # O Admin deleta o usuário Auth permanentemente. 
        # Se as chaves estrangeiras no Postgres estiverem em CASCADE, apaga profiles e transações.
        service_client.auth.admin.delete_user(user_id)
        return {"message": "Conta excluída permanentemente."}
    except Exception as e:
        logger.exception("Erro ao excluir conta")
        raise HTTPException(status_code=500, detail="Erro ao excluir conta.")

# --- ROTA DE UPLOAD DE AVATAR (BASE64) ---
@router.put("/avatar", status_code=200)
async def update_avatar(
    data: AvatarUpdate,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials
    user_id = get_user_id(token)
    db = get_authed_client(token)

    try:
        response = db.table("profiles").update({"avatar_url": data.avatar_url}).eq("id", user_id).execute()
        return {"message": "Avatar atualizado com sucesso!", "avatar_url": data.avatar_url}
    except Exception as e:
        logger.exception("Erro ao atualizar avatar")
        raise HTTPException(status_code=500, detail="Erro ao atualizar avatar.")
