from pydantic import BaseModel, Field


class ObjData(BaseModel):
    year: int
    price: float
    cpu_model: str = Field(alias='CPU model')
    hard_disk_size: str = Field(alias='Hard disk size')


class ResponseModel(BaseModel):
    id: str
    name: str
    data: ObjData


class DeleteResponseModel(BaseModel):
    message: str
