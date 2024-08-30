import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from markup.settings import AppSettings, ServerSettings
from markup.db.manager import DbManager
from markup.router import DbRouter


class WebAppFabric:
    def __init__(self, 
        db_manager: DbManager,
        app_settings: AppSettings,
        db_router: DbRouter
    ):
        self.db_manager = db_manager
        self.app_settings =  app_settings
        self.db_router = db_router

    @asynccontextmanager
    async def lifespan(self, app: FastAPI):
        await self.db_manager.prepare_db()
        yield

    def create_app(self):
        app = FastAPI(lifespan=self.lifespan)

        app.add_middleware(
            CORSMiddleware,
            allow_origins="*",
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        app.include_router(self.db_router.create_router())
        return app


class UvicornApp:
    def __init__(self, app: WebAppFabric, server_settings: ServerSettings):
        self.app = app
        self.server_settings = server_settings

    def start(self):
        uvicorn.run(
            self.app.create_app(),
            port=self.server_settings.port,
            host=self.server_settings.host,
        )