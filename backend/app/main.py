from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import router
from app.database import init_db

app = FastAPI(title="SentinelStream Banking Fraud Detection")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()
app.include_router(router)

@app.get("/")
def root():
    return {"status": "Backend running successfully"}  
