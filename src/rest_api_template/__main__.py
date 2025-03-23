from fastapi import FastAPI
import uvicorn
from .configs.env import APP_NAME, DEBUG_MODE, DATABASE_URL 

app = FastAPI()

@app.get("/")
async def root():
    return {
        "app_name": APP_NAME,
        "debug_mode": DEBUG_MODE,
        "database_url": DATABASE_URL
    }

def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("src.rest_api_template.__main__:app", host="0.0.0.0", port=8000, reload=True)
