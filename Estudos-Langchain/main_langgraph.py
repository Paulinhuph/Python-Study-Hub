from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from typing import Literal, TypedDict
from langgraph.graph import StateGraph, START, END
import asyncio
import os

load_dotenv()

llm = ChatOpenAI(
    model=os.getenv("LOCAL_MODEL"),
    api_key="lm-studio",
    base_url="http://127.0.0.1:1234/v1",
    temperature=0.7
)

llm_router = ChatOpenAI(
    model=os.getenv("LOCAL_MODEL"),
    api_key="lm-studio",
    base_url="http://127.0.0.1:1234/v1",
    temperature=0
)

prompt_consultor_praia = ChatPromptTemplate.from_messages([
    ("system", "Apresente-se como Sra Praia. Você é especialista em viagens com destino para praia."),
    ("human", "{query}")
])

prompt_consultor_montanha = ChatPromptTemplate.from_messages([
    ("system", "Apresente-se como Sr Montanha. Você é especialista em viagens com destino para montanhas e pontos turísticos radicais."),
    ("human", "{query}")
])

cadeia_praia = prompt_consultor_praia | llm | StrOutputParser()
cadeia_montanha = prompt_consultor_montanha | llm | StrOutputParser()

class Rota(TypedDict):# Importa o modelo de linguagem compatível com LangChain
from langchain_openai import ChatOpenAI

# Parser que converte a saída do modelo em string simples
from langchain_core.output_parsers import StrOutputParser

# Template para construção de prompts em formato de chat
from langchain_core.prompts import ChatPromptTemplate

# Carrega variáveis de ambiente do arquivo .env
from dotenv import load_dotenv

# Tipagens para estruturar dados de entrada e saída
from typing import Literal, TypedDict

# Componentes do LangGraph para construção de grafos de execução
from langgraph.graph import StateGraph, START, END

# Biblioteca para execução assíncrona
import asyncio

# Módulo para acessar variáveis de ambiente
import os


# Carrega variáveis do .env
load_dotenv()


# Modelo principal (respostas criativas)
llm = ChatOpenAI(
    model=os.getenv("LOCAL_MODEL"),  # Nome do modelo local
    api_key="lm-studio",             # Chave fictícia para endpoint local
    base_url="http://127.0.0.1:1234/v1",  # URL do servidor local
    temperature=0.7                  # Mais criatividade nas respostas
)


# Modelo secundário (roteador, mais determinístico)
llm_router = ChatOpenAI(
    model=os.getenv("LOCAL_MODEL"),
    api_key="lm-studio",
    base_url="http://127.0.0.1:1234/v1",
    temperature=0  # Baixa variabilidade → ideal para classificação
)


# Prompt para especialista em praias
prompt_consultor_praia = ChatPromptTemplate.from_messages([
    ("system", "Apresente-se como Sra Praia. Você é especialista em viagens com destino para praia."),
    ("human", "{query}")
])

# Prompt para especialista em montanhas
prompt_consultor_montanha = ChatPromptTemplate.from_messages([
    ("system", "Apresente-se como Sr Montanha. Você é especialista em viagens com destino para montanhas e pontos turísticos radicais."),
    ("human", "{query}")
])


# Cadeia para responder sobre praia
cadeia_praia = prompt_consultor_praia | llm | StrOutputParser()

# Cadeia para responder sobre montanha
cadeia_montanha = prompt_consultor_montanha | llm | StrOutputParser()


# Define o formato esperado do roteador
class Rota(TypedDict):
    destino: Literal["praia", "montanha"]


# Prompt que classifica a intenção do usuário
prompt_roteador = ChatPromptTemplate.from_messages([
    ("system",
     "Classifique a intenção do usuário e responda com um objeto cujo campo 'destino' seja apenas 'praia' ou 'montanha'. "
     "Use 'montanha' para trilhas, aventura, natureza, esportes radicais e pontos turísticos radicais. "
     "Use 'praia' para mar, areia, litoral, descanso à beira-mar."),
    ("human", "{query}")
])


# Cadeia de roteamento:
# Usa structured output para garantir resposta no formato Rota
roteador = prompt_roteador | llm_router.with_structured_output(Rota)


# Define o estado global do grafo
class Estado(TypedDict):
    query: str        # Pergunta do usuário
    destino: Rota     # Resultado do roteamento
    resposta: str     # Resposta final


# Nó 1: Roteador
# Decide se a pergunta vai para "praia" ou "montanha"
async def no_roteador(estado: Estado, config=None):
    resultado = await roteador.ainvoke({"query": estado["query"]}, config=config)

    # Debug para visualizar a decisão do modelo
    print("DEBUG destino roteado:", resultado)

    # Retorna o destino dentro do estado
    return {"destino": resultado}


# Nó 2: Especialista em praia
async def no_praia(estado: Estado, config=None):
    return {
        "resposta": await cadeia_praia.ainvoke(
            {"query": estado["query"]},
            config=config
        )
    }


# Nó 3: Especialista em montanha
async def no_montanha(estado: Estado, config=None):
    return {
        "resposta": await cadeia_montanha.ainvoke(
            {"query": estado["query"]},
            config=config
        )
    }


# Função que decide qual caminho o grafo seguirá
def escolher_no(estado: Estado) -> Literal["praia", "montanha"]:
    # Acessa o campo interno do dicionário retornado pelo roteador
    return estado["destino"]["destino"]


# Cria o grafo com o estado definido
grafo = StateGraph(Estado)

# Adiciona os nós ao grafo
grafo.add_node("rotear", no_roteador)
grafo.add_node("praia", no_praia)
grafo.add_node("montanha", no_montanha)


# Define fluxo:
# START → roteador
grafo.add_edge(START, "rotear")

# Roteador decide dinamicamente o próximo nó
grafo.add_conditional_edges("rotear", escolher_no)

# Ambos os caminhos terminam no END
grafo.add_edge("praia", END)
grafo.add_edge("montanha", END)


# Compila o grafo em uma aplicação executável
app = grafo.compile()


# Função principal assíncrona
async def main():
    # Executa o grafo com uma query inicial
    resposta = await app.ainvoke(
        {"query": "Quero um lugar em São Paulo com pontos turísticos radicais"}
    )

    # Exibe apenas a resposta final gerada
    print(resposta["resposta"])


# Executa o loop assíncrono
asyncio.run(main())
