from markup.db.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column

class Lesson(Base):
    __tablename__ = "lesso"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    order: Mapped[int]
    