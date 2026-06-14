from supabase import create_client, Client
from MoniaiAPIFAST.core.config import settings

# Cliente base anonimo — usado apenas para auth (login, register)
# NUNCA usar este cliente para queries de dados protegidos por RLS
supabase: Client = create_client(
    supabase_url=settings.SUPABASE_URL,
    supabase_key=settings.SUPABASE_ANON_KEY
)

def get_authed_client(token: str) -> Client:
    """
    Cria um cliente Supabase isolado e autenticado por requisição.
    Cada chamada retorna uma instância nova — sem compartilhamento entre usuários.
    Use este cliente em todas as rotas protegidas (transactions, categories, chat).
    """
    client: Client = create_client(
        supabase_url=settings.SUPABASE_URL,
        supabase_key=settings.SUPABASE_ANON_KEY
    )
    client.postgrest.auth(token)
    return client