from typing import Union

from pydantic import BaseModel


class NoticeBase(BaseModel):
    title: str
    msg_body: Union[str, None] = None


class NoticeCreate(NoticeBase):
    pass


class Notice(NoticeBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    firstname: str
    surname: str
    building: str
    apartment: int


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    notices: list[Notice] = []

    class Config:
        orm_mode = True
