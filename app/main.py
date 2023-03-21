from typing import Union
from fastapi import FastAPI, Path, Query
from app.routes import creditcard

app = FastAPI()

app.include_router(creditcard.router, tags=['CreditCards'], prefix='/api/credit-cards')

@app.get("/")
async def root():
    return "Everything is works!"