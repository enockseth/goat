from typing import TYPE_CHECKING, List

from sqlmodel import Column, Field, Relationship, SQLModel, Text

from src.db.models.user import UserRole

if TYPE_CHECKING:
    from .customization import Customization
    from .user import User

from ._link_model import UserRole


class Role(SQLModel, table=True):
    __tablename__ = "role"
    __table_args__ = {"schema": "customer"}

    id: int = Field(primary_key=True)
    name: str = Field(sa_column=Column(Text, nullable=False))

    customizations: List["Customization"] = Relationship(back_populates="role")
    users: List["User"] = Relationship(back_populates="roles", link_model=UserRole)
