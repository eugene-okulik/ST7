from pydantic import BaseModel, Field


class ObjData(BaseModel):
    year: int
    price: str
    CPU_model: str = Field(alias='CPU model')
    Hard_disk_size: str = Field(alias='Hard disk size')


class NewObjWithData(BaseModel):
    name: str
    data: ObjData


class DelNewObjWithData(BaseModel):
    message: str
