from pydantic import BaseModel, Field
from typing import Any


class DeleteSingleObject(BaseModel):
    message: str


class ObjData(BaseModel):
    id: str
    name: str
    createdAt: str
    data: dict[str, Any]
