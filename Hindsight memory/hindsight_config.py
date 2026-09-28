import os
from pathlib import Path

from dotenv import load_dotenv
from hindsight_client import Hindsight

# Load .env from the DataDrift root folder
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

HINDSIGHT_BASE_URL = os.getenv(
    "HINDSIGHT_BASE_URL",
    "https://api.hindsight.vectorize.io"
)

HINDSIGHT_API_KEY = os.getenv("HINDSIGHT_API_KEY")

BANK_ID = os.getenv(
    "HINDSIGHT_BANK_ID",
    "datadrift-sales"
)

if not HINDSIGHT_API_KEY:
    raise ValueError(
        "HINDSIGHT_API_KEY is not set in .env"
    )

client = Hindsight(
    base_url=HINDSIGHT_BASE_URL,
    api_key=HINDSIGHT_API_KEY
)