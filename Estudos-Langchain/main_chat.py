# Importa o módulo os para acessar variáveis de ambiente do sistema
import os

# Importa a função load_dotenv para carregar variáveis do arquivo .env
from dotenv import load_dotenv

# Importa o modelo de chat compatível com LangChain
from langchain_openai import ChatOpenAI

# Importa o template de prompt para conversas com múltiplas mensagens
from langchain_core.prompts import ChatPromptTemplate

# Importa o parser que converte a saída do modelo em texto simples
from langchain_core.output_parsers import StrOutputParser

# Importa uma implementação de histórico de mensagens armazenado em memória
from langchain_core.chat_history import InMemoryChatMessageHistory

# Importa o wrapper que adiciona memória de conversa a uma cadeia
from langchain_core.runnables.history import RunnableWithMessageHistory


# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()


# Cria a instância do modelo de linguagem
llm = ChatOpenAI(
    # Nome do modelo definido na variável de ambiente LOCAL_MODEL
    model=os.getenv("LOCAL_MODEL"),

    # Chave fictícia usada com LM Studio/local endpoint
    api_key="lm-studio",

    # Endpoint local compatível com API OpenAI
    base_url="http://127.0.0.1:1234/v1",

    # Controla o grau de criatividade/variação das respostas
    temperature=0.5
)


# Cria o prompt de conversa com mensagens em formato de chat
prompt_sugestao = ChatPromptTemplate.from_messages(
[
    # Mensagem de sistema: define o comportamento e identidade da IA
    ("system", "Você é um guia de viagem especializado em destinos brasileiros. Apresente-se como Sr. Passeios"),

    # Placeholder onde o histórico da conversa será inserido automaticamente
    ("placeholder", "{historico}"),

    # Mensagem do usuário, recebida dinamicamente pela variável query
    ("human", "{query}")
]
)


# Monta a cadeia principal:
# 1. gera o prompt
# 2. envia para o modelo
# 3. converte a resposta para string
cadeia = prompt_sugestao | llm | StrOutputParser()


# Dicionário que armazenará o histórico de conversa de cada sessão
memoria = {}

# Identificador fixo da sessão atual
sessao = "aula_langchain_alura"


# Função responsável por recuperar ou criar o histórico de uma sessão
def historico_por_sessao(sessao: str):
    # Se a sessão ainda não existir na memória, cria um histórico vazio
    if sessao not in memoria:
        memoria[sessao] = InMemoryChatMessageHistory()

    # Retorna o histórico correspondente à sessão
    return memoria[sessao]


# Lista de perguntas que serão enviadas em sequência
lista_perguntas = [
    "Quero visitar um lugar no Brasil, famoso por praias e cultura. Pode sugerir?",
    "Qual a melhor época do ano para ir?"
]


# Cria uma nova cadeia com suporte a memória de conversa
cadeia_com_memoria = RunnableWithMessageHistory(
    # Cadeia original que será executada
    runnable=cadeia,

    # Função que recupera o histórico com base no id da sessão
    get_session_history=historico_por_sessao,

    # Nome da chave do dicionário de entrada que contém a nova mensagem do usuário
    input_messages_key="query",

    # Nome da chave usada no prompt para inserir o histórico
    history_messages_key="historico"
)


# Percorre cada pergunta da lista
for uma_pergunta in lista_perguntas:
    # Executa a cadeia com memória
    resposta = cadeia_com_memoria.invoke(
        {
            # Passa a pergunta atual como entrada
            "query": uma_pergunta
        },
        # Define a sessão usada para recuperar e atualizar o histórico
        config={"session_id": sessao}
    )

    # Exibe a pergunta do usuário
    print("Usuário: ", uma_pergunta)

    # Exibe a resposta da IA
    print("IA: ", resposta, "\n")
