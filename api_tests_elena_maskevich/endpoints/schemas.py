from pydantic import BaseModel
from typing import Any


class CreatedObject(BaseModel):
    id: str
    name: str
    createdAt: str
    data: dict[str, Any]


class DeletedObject(BaseModel):
    message: str
