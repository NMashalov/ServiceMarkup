from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from markup.db.models.base import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    telegram_login: Mapped[str] = mapped_column(
        String(100), unique=True, index=True, nullable=False
    )
