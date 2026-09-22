from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "Aurora API"
    app_env: str = "development"
    secret_key: str = "change-me"
    database_url: str = "sqlite:///./app.db"
    demo_user: str = "demo"
    demo_password: str = "demo123"


settings = Settings()
