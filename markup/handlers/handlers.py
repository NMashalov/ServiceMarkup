from fastapi.responses import Response
from markup.repository.user import UserRepository
from markup.models import RegisterRequest

class Dbhandlers:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def get_by_id(self,user_id: int):
        user_login = await self.repository.get_by_id(user_id=user_id)
        return user_login
    
    async def create_by_id(self,user_id: int, registre_request: RegisterRequest):
        await self.repository.create(user_id=user_id,telegram_login=registre_request.telegram_login)
        return Response(content='ok')
    