import uuid
from datetime import date
from sqlmodel import SQLModel, Field
from app.utils.list_status import StatusType
import sqlalchemy as sa
from sqlalchemy import Enum as SAEnum


class Todo(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str = Field(max_length=255, min_length=1)
    desc: str | None = Field(default=None, max_length=1000)
    status: StatusType = Field(default=StatusType.pending, sa_column=sa.Column(SAEnum(StatusType), nullable=False))
    deadline: date