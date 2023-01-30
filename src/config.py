from pydantic import BaseSettings

# connect_url para uso com o docker compose: mysql+pymysql://root:password@db/db
class Settings(BaseSettings):
    db_connect_url: str = ""

    class Config:
        env_file = ".env"

settings = Settings()
