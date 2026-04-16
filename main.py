from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from classify_user_intent import classify_user_intent
from answer_user_query import answer_user_query


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
    user_intent = classify_user_intent(request.input)
    print(user_intent)
    result = answer_user_query(user_intent.strip(),request.input)

    return {"status": "ok", "result": result}


