from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from markup.db.manager import DbManager
from markup.db.models.user import User
from markup.repository.exceptions import NotFoundError


class UserNotFoundError(NotFoundError):
    entity_name: str = "User"

class UserRepository:
    def __init__(self, db_manager: DbManager):
        self.a_session_factory = db_manager.a_sessionmaker

    async def get_by_id(self, user_id: int) -> User:
        async with self.a_session_factory() as a_session:
            user = await a_session.execute(select(User))
            materialized_user = user.scalar_one()
            if not materialized_user:
                raise UserNotFoundError(user_id)
            return materialized_user
        
    async def delete_by_id(self, user_id: int) -> None:
        with self.a_session_factory() as session:
            entity: User = session.query(User).filter(User.id == user_id).first()
            if not entity:
                raise UserNotFoundError(user_id)
            session.delete(entity)
            session.commit()
        
    async def create(self, user_id: int, telegram_login: str,) -> User:
        async with self.a_session_factory() as a_session:
            user = User(
                id = user_id,
                telegram_login=telegram_login,
            )
            a_session.add(user)
            a_session.refresh()
            try:
                await a_session.commit()
            except IntegrityError:
                return None
