from typing import Union
from datetime import date
from pydantic import BaseModel


class CompanyBase(BaseModel):
    name: str
    address: Union[str, None] = None
    phonenumber: str
    website: Union[str, None] = None
    industry: str
    size: int
    founded: date


class CompanyCreate(CompanyBase):
    pass


class Company(CompanyBase):
    id: int

    class Config:
        orm_mode = True
