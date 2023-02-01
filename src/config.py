from pydantic import BaseSettings

# connect_url para uso com o docker compose: mysql+pymysql://root:password@db/db
class Settings(BaseSettings):
    # db_connect_url: str = "mysql+pymysql://root:password@db/db"
    db_connect_url: str = "mysql+pymysql://amisroot:vgHNQB0HVxP07iFd3YFO@amis.mysql.database.azure.com/amisdb"

    class Config:
        env_file = ".env"

settings = Settings()
