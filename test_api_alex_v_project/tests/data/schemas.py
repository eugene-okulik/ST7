from pydantic import BaseModel, Field


class DeleteSingleObject(BaseModel):
    message: str


class ObjData(BaseModel):
    year: int
    price: int
    cpu_value: str = Field(alias='CPU model')
    disk_size: str = Field(alias='Hard disk size')
