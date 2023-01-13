from pydantic import BaseSettings

# "mysql+pymysql://amis_admin:Master1234@amis-stg-server.mysql.database.azure.com/amisdb-stg"
class Settings(BaseSettings):
    db_connect_url: str = "mysql+pymysql://root:password@db/db"

    class Config:
        env_file = ".env"

settings = Settings()