# Placeholder FastAPI backend
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "DreamWeaver AI backend alive"}
