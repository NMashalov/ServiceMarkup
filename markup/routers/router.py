from fastapi import APIRouter
from markup.handlers import Dbhandlers


class UserRouter:
    GET_ID: str = '/user/{user_id}'
    CREATE_USER: str = '/user/{user_id}/create'

    TAGS = ['DB']

    def __init__(self,db_handlers: Dbhandlers):
        self._db_handlers = db_handlers

    def create_router(self):
        router = APIRouter(tags =self.TAGS)

        router.add_api_route(
            path=self.GET_ID,
            endpoint=self._db_handlers.get_by_id,
            methods=['GET']
        )
        router.add_api_route(
            path=self.CREATE_USER,
            endpoint=self._db_handlers.create_by_id,
            methods=['POST']
        )
        return router
