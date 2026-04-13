from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import get_weather_report


app = FastAPI(title="Invader API", version="1.0.0")


class QueryRequest(BaseModel):
    input: str


@app.get("/")
def root():
    return {"message": "Welcome to the Jarvis"}


@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/jarvis")
def jarvis(request: QueryRequest):
    result = get_weather_report(request.input)
    return {"status": "ok", "result": result}


