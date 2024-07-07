from pydantic import BaseModel, Field


class Data(BaseModel):
    year: int
    price: float
    cpu_model: str = Field(alias='CPU model')
    hard_disk_size: str = Field(alias='Hard disk size')


class Device(BaseModel):
    id: str
    name: str
    createdAt: str
    data: Data


class GetDevice(BaseModel):
    id: str
    name: str
    data: Data


class PutDevice(BaseModel):
    id: str
    name: str
    updatedAt: str
    data: Data


class DelDevice(BaseModel):
    message: str


class DelNotExistDevice(BaseModel):
    error: str
