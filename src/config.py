from pydantic import BaseSettings

class Settings(BaseSettings):
    db_connect_url: str

    class Config:
        env_file = ".env"

settings = Settings()
