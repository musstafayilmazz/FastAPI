from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional
from functools import lru_cache
from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()

class BaseConfig(BaseSettings):
    ENV_STATE: Optional[str] = os.getenv('ENV_STATE', 'dev')  # Provide a default value
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

class GlobalConfig(BaseConfig):
    DATABASE_URL: Optional[str] = None
    DB_FORCE_ROLLBACK: bool = False

class DevConfig(GlobalConfig):
    model_config = SettingsConfigDict(env_prefix="DEV_")

class TestConfig(GlobalConfig):
    DATABASE_URL: str = "postgresql://postgres:postgres@172.25.0.2:5432/db_storeapi"
    DB_FORCE_ROLLBACK: bool = True

class ProdConfig(GlobalConfig):
    model_config = SettingsConfigDict(env_prefix="PROD_")

@lru_cache()
def get_config(env_state: str):
    configs = {"dev": DevConfig, "test": TestConfig, "prod": ProdConfig}
    return configs[env_state]()

config = get_config(BaseConfig().ENV_STATE)
