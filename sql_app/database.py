from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import asyncio

SQLALCHEMY_DATABASE_URL = "sqlite:///akihabara.db"
# SQLALCHEMY_DATABASE_URL = "mysql+asyncmy://root:remotecontrol@localhost:3306/smart_yard"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL #, pool_pre_ping=True #, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
