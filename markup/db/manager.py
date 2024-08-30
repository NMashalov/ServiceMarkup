from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker
from markup.db.settings import DbSettings
from markup.db.models.base import Base


class DbManager:
    CHAT_TABLE_NAME = "CHAT"

    def __init__(self, settings: DbSettings):

        self.a_sqlalchemy_engine = create_async_engine(
            settings.conn_string, echo=True
        )
        self.a_sessionmaker = async_sessionmaker(
            self.a_sqlalchemy_engine, expire_on_commit=False
        )

    async def prepare_db(self):
        async with self.a_sqlalchemy_engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)