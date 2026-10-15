import os
from decimal import Decimal
from pathlib import Path

from dotenv import load_dotenv

# Load .env file from backend root if present
_backend_dir = Path(__file__).resolve().parent.parent.parent
_env_file = _backend_dir / ".env"
if _env_file.exists():
    load_dotenv(_env_file)
else:
    load_dotenv()


class Settings:
    def __init__(self):
        self.APP_NAME: str = os.getenv("APP_NAME", "PharmaKon")
        self.APP_VERSION: str = os.getenv("APP_VERSION", "0.1.0")
        self.API_V1_PREFIX: str = os.getenv("API_V1_PREFIX", "/api/v1")
        self.DEBUG: bool = os.getenv("DEBUG", "True").lower() in ("true", "1", "t", "yes")
        self.DEFAULT_PAGE_SIZE: int = int(os.getenv("DEFAULT_PAGE_SIZE", "20"))
        self.MAX_PAGE_SIZE: int = int(os.getenv("MAX_PAGE_SIZE", "100"))
        self.VAT_RATE: Decimal = Decimal(os.getenv("VAT_RATE", "13.00"))
        self.EXPIRY_ALERT_DAYS: int = int(os.getenv("EXPIRY_ALERT_DAYS", "60"))

        # Database Configuration (PostgreSQL 15+ target)
        self.DATABASE_URL: str = os.getenv(
            "DATABASE_URL",
            "postgresql+psycopg://postgres:postgres@localhost:5432/pharmakon",
        )
        self.DB_ECHO: bool = os.getenv("DB_ECHO", "False").lower() in ("true", "1", "t", "yes")


settings = Settings()
