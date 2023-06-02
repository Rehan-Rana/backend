from typing import Union
from datetime import date
from pydantic import BaseModel


class CompanyBase(BaseModel):
    name: str
    address: Union[str, None] = None
    phone_number: str
    website: Union[str, None] = None
    industry: str
    size: int
    founded: date


class CompanyCreate(CompanyBase):
    pass


class CompanyUpdate(CompanyBase):
    pass


class Company(CompanyBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    is_active: bool


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
