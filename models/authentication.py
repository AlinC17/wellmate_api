from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import String

from utilities.database.models import Base


class User(Base):
    __tablename__ = 'users'
    username: Mapped[str] = mapped_column(String(15), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(25), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(16), nullable=False)
    first_name: Mapped[str] = mapped_column(String(15), nullable=False)
    last_name: Mapped[str] = mapped_column(String(15), nullable=False)

""" To be continued... JWT implementation planned """
