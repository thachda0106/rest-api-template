import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World1"}

def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("src.rest_api_template.main:app", host="0.0.0.0", port=8000, reload=True)
