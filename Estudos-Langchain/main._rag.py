from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEmbeddings
import os

load_dotenv()

# 1) Modelo local via LM Studio
llm = ChatOpenAI(
    model=os.getenv("LOCAL_MODEL"),
    api_key="lm-studio",
    base_url="http://127.0.0.1:1234/v1",
    temperature=0.2
)

# 2) Embeddings locais
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 3) PDFs
arquivos = [
    "documentos/GTB_standard_Nov23.pdf",
    "documentos/GTB_gold_Nov23.pdf",
    "documentos/GTB_platinum_Nov23.pdf"
]

# 4) Carregar todos os documentos
documentos = []
for arquivo in arquivos:
    docs = PyMuPDFLoader(arquivo).load()
    documentos.extend(docs)

# 5) Limpeza simples do texto extraído do PDF
for doc in documentos:
    texto = doc.page_content
    texto = texto.replace("\n", " ")
    texto = " ".join(texto.split())  # remove espaços repetidos
    doc.page_content = texto

# 6) Separar em pedaços melhores para PDF
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=150
)

pedacos = splitter.split_documents(documentos)

# 7) Criar base vetorial + retriever
retriever = FAISS.from_documents(
    pedacos,
    embeddings
).as_retriever(search_kwargs={"k": 4})

# 8) Prompt mais rígido
prompt_consulta_seguro = ChatPromptTemplate.from_messages([
    (
        "system",
        "Responda usando exclusivamente o conteúdo fornecido no contexto. "
        "Se a informação não estiver claramente presente, diga: "
        "'Não encontrei informação suficiente no documento.' "
        "Seja direto, específico e fiel ao texto."
    ),
    (
        "human",
        "Pergunta: {query}\n\nContexto:\n{contexto}\n\nResposta:"
    )
])

cadeia = prompt_consulta_seguro | llm | StrOutputParser()

# 9) Função para responder com debug
def responder(pergunta: str):
    trechos = retriever.invoke(pergunta)

    print("\n=== TRECHOS RECUPERADOS ===")
    for i, trecho in enumerate(trechos, start=1):
        print(f"\n--- Trecho {i} ---")
        print(trecho.page_content[:700])

    contexto = "\n\n".join(trecho.page_content for trecho in trechos)

    print("\n=== CONTEXTO ENVIADO AO MODELO ===")
    print(contexto[:2000])

    resposta = cadeia.invoke({
        "query": pergunta,
        "contexto": contexto
    })

    return resposta

# 10) Teste
print("\n=== RESPOSTA FINAL ===")
print(responder("Quais são os benefícios do cartão Mastercard Gold?"))
