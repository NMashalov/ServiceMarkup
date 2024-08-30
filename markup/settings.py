from pydantic_settings import BaseSettings, SettingsConfigDict


class ServerSettings(BaseSettings):
    host: str = '0.0.0.0'
    port: int = 5000

    model_config = SettingsConfigDict(env_file=".env", env_prefix="UNICORN_",extra='ignore')


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="APP_",extra='ignore')
