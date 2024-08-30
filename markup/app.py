import uvicorn
from markup.web import UvicornApp,WebAppFabric
from markup.db.manager import DbManager
from markup.db.settings import DbSettings
from markup.settings import ServerSettings, AppSettings
from markup.routers import DbRouter
from markup.handlers import Dbhandlers
from markup.db.repository.user import UserRepository

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

def create_app():
    db_manager = DbManager(
        settings= DbSettings()
    )
    return UvicornApp(
        app = WebAppFabric(
            db_manager=db_manager,
            app_settings=AppSettings(),
            db_router = DbRouter(
                Dbhandlers(
                    repository=UserRepository(
                        db_manager=db_manager
                    )
                )
            )
        ),
        server_settings=ServerSettings()
    )