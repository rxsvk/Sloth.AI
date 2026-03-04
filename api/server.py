from fastapi import FastAPI
from core.brain import think

app = FastAPI()

@app.get("/")
def home():
    return {"status": "SLOTH AI running"}

@app.get("/think")
def ai(q: str):

    response = think(q)

    return {"response": response}
