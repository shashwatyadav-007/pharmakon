from decimal import Decimal

class Settings:
    APP_NAME: str = "PharmaKon"
    APP_VERSION: str = "0.1.0"
    API_V1_PREFIX: str = "/api/v1"
    DEBUG: bool = True
    DEFAULT_PAGE_SIZE: int = 20
    MAX_PAGE_SIZE: int = 100
    VAT_RATE: Decimal = Decimal("13.00")
    EXPIRY_ALERT_DAYS: int = 60

settings = Settings()
