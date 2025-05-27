from fastapi import FastAPI
from . import dml,loaddemo,models
from .database import engine

app=FastAPI()

models.Base.metadata.create_all(bind=engine)
app.include_router(dml.router)
app.include_router(loaddemo.router)