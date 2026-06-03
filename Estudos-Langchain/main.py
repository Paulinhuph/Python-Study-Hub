# Importa o módulo os, usado aqui para acessar variáveis de ambiente
import os

# Carrega variáveis de ambiente a partir de um arquivo .env
from dotenv import load_dotenv

# Classe de modelo de linguagem da OpenAI compatível com LangChain
from langchain_openai import ChatOpenAI

# Classe para criação de prompts com variáveis dinâmicas
from langchain_core.prompts import PromptTemplate

# Parsers de saída:
# - JsonOutputParser: converte a resposta em JSON validado por um modelo Pydantic
# - StrOutputParser: converte a resposta para string simples
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser

# Pydantic é usado para definir estruturas de dados com validação
from pydantic import Field, BaseModel


# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()


# Modelo de saída esperado para a recomendação de destino
class Destino(BaseModel):
    # Campo que representa a cidade sugerida
    cidade: str = Field("A cidade recomendada para visitar")

    # Campo que representa o motivo da recomendação
    motivo: str = Field("motivo pelo qual é interessante visitar essa cidade")


# Modelo de saída esperado para a recomendação de restaurantes
class Restaurantes(BaseModel):
    # Campo que representa a cidade recomendada
    cidade: str = Field("A cidade recomendada para visitar")

    # Campo que representa os restaurantes sugeridos para a cidade
    restaurantes: str = Field("Restaurantes recomendados na cidade")


# Parser que transforma a saída do modelo em JSON no formato da classe Destino
parseador_destino = JsonOutputParser(pydantic_object=Destino)

# Parser que transforma a saída do modelo em JSON no formato da classe Restaurantes
parseador_restaurantes = JsonOutputParser(pydantic_object=Restaurantes)


# Prompt que pede ao modelo para sugerir uma cidade com base em um interesse
prompt_cidade = PromptTemplate(
    input_variables=["interesse"],  # variável esperada no momento da execução
    template="""Sugira uma cidade dado o meu interesse por {interesse}. {formato_de_saida}""",
    # partial_variables injeta automaticamente as instruções de formato JSON
    partial_variables={"formato_de_saida": parseador_destino.get_format_instructions()}
)

# Prompt que pede ao modelo restaurantes populares na cidade informada
prompt_restaurantes = PromptTemplate(
    template="""Sugira restaurantes populares entre locais em {cidade}. {formato_de_saida}""",
    # instruções para obrigar a saída no formato do modelo Restaurantes
    partial_variables={"formato_de_saida": parseador_restaurantes.get_format_instructions()}
)

# Prompt simples para sugerir atividades e locais culturais em uma cidade
prompt_cultural = PromptTemplate(
    template="Sugira atividades e locais em {cidade}"
)


# Configuração do modelo LLM
llm = ChatOpenAI(
    # Nome do modelo carregado a partir da variável de ambiente LOCAL_MODEL
    model=os.getenv("LOCAL_MODEL"),

    # Chave fictícia usada porque o LM Studio geralmente exige um valor, mesmo localmente
    api_key="lm-studio",

    # URL local do servidor compatível com API OpenAI
    base_url="http://127.0.0.1:1234/v1",

    # Controla o nível de criatividade da resposta
    temperature=0.7
)

# Cadeia 1:
# 1. monta o prompt da cidade
# 2. envia para o modelo
# 3. faz o parse da resposta para o formato JSON definido em Destino
cadeia_1 = prompt_cidade | llm | parseador_destino

# Cadeia 2:
# 1. monta o prompt de restaurantes
# 2. envia para o modelo
# 3. faz o parse da resposta para o formato JSON definido em Restaurantes
cadeia_2 = prompt_restaurantes | llm | parseador_restaurantes

# Cadeia 3:
# 1. monta o prompt cultural
# 2. envia para o modelo
# 3. converte a resposta final para texto simples
cadeia_3 = prompt_cultural | llm | StrOutputParser()

# Importa RunnableLambda, que permite inserir uma função Python
# dentro da pipeline do LangChain
from langchain_core.runnables import RunnableLambda

# Cadeia principal composta:
cadeia = (
    cadeia_1
    # Primeiro gera uma cidade com base no interesse
    | cadeia_2
    # Depois usa a cidade retornada para sugerir restaurantes
    | RunnableLambda(lambda x: {"cidade": x["cidade"]})
    # Aqui filtra apenas o campo "cidade" da saída anterior,
    # pois o próximo prompt só precisa dessa informação
    | cadeia_3
    # Por fim, usa a cidade para sugerir atividades e locais
)

# Exibe na tela o objeto do prompt da primeira cadeia
print("Prompt:", prompt_cidade)

# Executa a cadeia completa passando o interesse "praias"
resposta = cadeia.invoke({"interesse": "praias"})

# Mostra a resposta final gerada pela última etapa da cadeia
print(resposta)
