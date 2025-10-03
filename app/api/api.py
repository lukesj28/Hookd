from fastapi import FastAPI, Security
from app.api.utils import VerifyToken

app = FastAPI()
auth = VerifyToken()

@app.get("/api/")
def private(auth_result: str = Security(auth.verify)):
    return auth_result