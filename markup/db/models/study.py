from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from markup.db.models.base import Base
from datetime import datetime


class Assigment(Base):
    __tablename__ = 'rentals'
    id: Mapped[int]= mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    lesson_id: Mapped[int] = mapped_column(ForeignKey('books.id'))
    rental_date: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    return_date: Mapped[datetime] = mapped_column(nullable=True)

    user = relationship('User')
    book = relationship('Book')