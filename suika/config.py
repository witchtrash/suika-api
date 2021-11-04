from functools import lru_cache
from pydantic import BaseSettings

class Settings(BaseSettings):
  app_name: str
  database_host: str
  database_user: str
  database_password: str

  class Config:
    env_file = '.env'


@lru_cache()
def get_settings():
  return Settings()

@lru_cache()
def get_test_settings():
  return Settings(
    _env_file='.env.testing'
  )
