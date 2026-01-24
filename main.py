from fastapi import FastAPI
from app.routers.carga_gastos import router

app = FastAPI()
app.include_router(router)
