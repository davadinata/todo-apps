from datetime import date
from sqlmodel import SQLModel, Field
from uuid import UUID
from app.utils.list_status import StatusType


class TodoResponse(SQLModel):
    id: UUID
    title: str
    desc: str | None = None
    status: StatusType = StatusType.pending
    deadline: date


class TodoRequest(SQLModel):
    title: str = Field(max_length=255, min_length=1)
    desc: str | None = Field(default=None, max_length=1000)
    deadline: date
    status: StatusType = StatusType.pending


class TodoUpdateRequest(SQLModel):
    title: str | None = Field(default=None, max_length=255, min_length=1)
    desc: str | None = Field(default=None, max_length=1000)
    status: StatusType | None = None
    deadline: date | None = None