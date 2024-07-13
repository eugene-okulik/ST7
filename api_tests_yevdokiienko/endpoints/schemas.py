from pydantic import BaseModel, Field


class ObjectData(BaseModel):
    year: int
    price: float
    CPU_model: str = Field(alias='CPU model')
    Hard_disk_size: str = Field(alias='Hard disk size')


class NewObjectData(BaseModel):
    id: str
    name: str
    createdAt: str
    data: ObjectData


class DeleteObjData(BaseModel):
    message: str
