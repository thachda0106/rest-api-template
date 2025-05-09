from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
import uvicorn

from .db.engine import init_db
from fastapi.middleware.cors import CORSMiddleware
from .configs.env import ORIGINS

from .modules.tasks.router import router as tasks_router
from .modules.links.router import router as links_router

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
app.include_router(tasks_router, prefix="/api/v1")
app.include_router(links_router, prefix="/api/v1")
