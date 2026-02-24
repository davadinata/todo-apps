from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env"
    )

    APP_NAME: str = "Todo Apps"
    VERSION: str = "0.0.1"
    DB_URL: str = "sqlite:///database.db"


settings = Settings()