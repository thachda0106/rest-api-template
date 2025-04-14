from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
import uvicorn
from .routers import tasks, links
from .db.engine import init_db
from fastapi.middleware.cors import CORSMiddleware
from .configs.env import ORIGINS

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def start():
    """Server run at http://localhost:8000"""
    uvicorn.run(
        "src.rest_api_template.__main__:app", host="0.0.0.0", port=8000, reload=True
    )

# ROUTES
app.include_router(tasks.router, prefix="/api/v1")
app.include_router(links.router, prefix="/api/v1")
