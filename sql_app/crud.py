from sqlalchemy.orm import Session

import models, schemas



def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_names(db: Session, firstname: str, surname: str):
    return db.query(models.User).filter(models.User.firstname == firstname, models.User.surname == surname).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(firstname=user.firstname, surname=user.surname, building=user.building, apartment=user.apartment,  hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_notices(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Notice).offset(skip).limit(limit).all()


def create_user_notice(db: Session, notice: schemas.NoticeCreate, user_id: int):
    db_notice = models.Notice(**notice.dict(), owner_id=user_id)
    db.add(db_notice)
    db.commit()
    db.refresh(db_notice)
    return db_notice

def delete_user(db: Session, user_id: int):
    db_deleted = db.query(models.User).filter(models.User.id == user_id).first()
    db.delete(db_deleted)
    return db_deleted

def get_buildings_list(db: Session, skip: int = 0, limit: int = 100):
    buildings = list(set(db.query(models.User.building).all()))
    return buildings

def get_apartments_list_by_building(db: Session, building: str, skip: int = 0, limit: int = 100):
    apartment = list(set(db.query(models.User.apartment).filter(models.User.building == building).all()))
    return apartment
