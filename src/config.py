from pydantic import BaseSettings

class Settings(BaseSettings):
    db_connect_url: str = "mysql+pymysql://amisroot:vgHNQB0HVxP07iFd3YFO@http://amis.mysql.database.azure.com/amisdb-stg"

    class Config:
        env_file = ".env"

settings = Settings()
