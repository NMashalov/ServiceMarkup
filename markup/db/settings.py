from pydantic_settings import BaseSettings, SettingsConfigDict


class DbSettings(BaseSettings):
    user: str
    password: str
    host: str
    port: str
    database: str

    @property
    def conn_string(self):
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}/{self.database}"

    model_config = SettingsConfigDict(env_file=".env", env_prefix="PG_",extra='ignore')
