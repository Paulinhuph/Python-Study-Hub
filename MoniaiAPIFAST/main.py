from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from MoniaiAPIFAST.core.config import settings
from MoniaiAPIFAST.routers import auth, transactions, analytics, categories, chat
app = FastAPI(title="AlFinance API")

# Lista de origens permitidas 
list_run = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5500",  
    "http://localhost:5500",
    "https://moni-ai.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=list_run,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router,         prefix="/api")
app.include_router(transactions.router, prefix="/api")
app.include_router(analytics.router,    prefix="/api")
app.include_router(categories.router,   prefix="/api")
app.include_router(chat.router,         prefix="/api")  

@app.get("/")
async def root():
    return {"status": "FinancAl API Rodando"}