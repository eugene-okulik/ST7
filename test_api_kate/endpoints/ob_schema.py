from pydantic import BaseModel, Field


class ObjData(BaseModel):
    year: int
    price: float
    CPU_model: str = Field(alias='CPU model')
    hard_disk_size: str = Field(alias='Hard disk size')


class NewObjWithData(BaseModel):
    id: str
    name: str
    data: ObjData


class DeletedObject(BaseModel):
    message: str
