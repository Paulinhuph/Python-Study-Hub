import jwt
import logging
from fastapi import HTTPException, status
from MoniaiAPIFAST.core.config import settings

logger = logging.getLogger(__name__)

def get_user_id(token: str) -> str:
    """
    Valida a assinatura e expiração do token JWT do Supabase.
    Retorna o user_id (sub) com segurança real — tokens forjados são rejeitados.
    """
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.JWT_ALGORITHM],
            options={"verify_exp": True},
            audience="authenticated",
        )

        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido: identificador do usuário ausente.",
            )
        return user_id

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Sessão expirada. Por favor, faça login novamente.",
        )
    except (jwt.InvalidSignatureError, jwt.InvalidTokenError) as e:
        logger.warning("Token JWT rejeitado: %s", e)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token de autorização inválido ou corrompido.",
        )