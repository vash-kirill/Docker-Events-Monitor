from pydantic import BaseConfig
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    logLevel: str = "INFO"
    configPath: str = "config/config.yml"

    sentry_dsn: str = ""
    sentry_env: str = "production"

    class Config(BaseConfig):
        case_sensitive: bool = False
        env_file = ".env"

settings = Settings()
