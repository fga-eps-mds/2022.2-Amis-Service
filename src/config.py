from pydantic import BaseSettings

class Settings(BaseSettings):
    db_connect_url: str = "mysql+pymysql://root:password@db/db"

    class Config:
        env_file = ".env"

settings = Settings()