from pydantic import BaseModel, Field


class ObjData(BaseModel):
    year: int
    price: float
    cpu_model: str = Field(alias='CPU model')
    hard_disk: str = Field(alias='Hard disk size')


class ResponseSchema(BaseModel):
    id: str
    name: str
    data: ObjData


class DeleteResponseSchema(BaseModel):
    message: str
