from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/", StaticFiles(directory="static", html=True), name="static")

@app.get("/api")
def home():
    return {"message": "GLTF Streaming Server Running 🚀"}