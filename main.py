from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Invader API", version="1.0.0")



@app.get("/")
def root():
    return {"message": "Welcome to the Jarvis"}


@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/jarvis")
def jarvis(input):
    user_input 
    return {"status": "ok"}


