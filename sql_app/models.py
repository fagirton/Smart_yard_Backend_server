from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, unique=False, index=True)
    surname = Column(String, unique=False, index=True)
    building = Column(String, unique=False, index=True)
    apartment = Column(Integer, unique=False, index=True)
    hashed_password = Column(String)

    notices = relationship("Notice", back_populates="owner")


class Notice(Base):
    __tablename__ = "notices"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    msg_body = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="notices")
