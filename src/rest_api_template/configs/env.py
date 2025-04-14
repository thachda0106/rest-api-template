from dotenv import load_dotenv
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]
load_dotenv(BASE_DIR / ".env")

# APP ENVS
APP_NAME = os.getenv("APP_NAME")
DEBUG_MODE = os.getenv("DEBUG")
DATABASE_URL = os.getenv("DATABASE_URL")
ORIGINS=os.getenv("ORIGINS").split(',')
