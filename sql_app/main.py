from json import JSONDecoder, JSONEncoder
from fastapi import Depends, FastAPI, HTTPException
from pydantic import JsonWrapper
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine
from crud import get_apartments_list_by_building, get_buildings_list


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_names(db, firstname=user.firstname, surname=user.surname)
    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/notices/", response_model=schemas.Notice)
def create_notice_for_user(user_id: int, notice: schemas.NoticeCreate, db: Session = Depends(get_db)):
    return crud.create_user_notice(db=db, notice=notice, user_id=user_id)


@app.get("/notices/", response_model=list[schemas.Notice])
def read_notices(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    notices = crud.get_notices(db, skip=skip, limit=limit)
    return notices

@app.delete('/users/delete/{user_id}', name="Удалить пользователя", response_model=schemas.User)
def delete_user(user_id: int):
    deleted_user = delete_user(user_id)
    return deleted_user

@app.get("/buildings/", response_model=list)
def read_buildings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    buildings = get_buildings_list(db, skip=skip, limit=limit)
    return buildings

# @app.get("/apartments/", response_model=list)
# def read_apartments(building, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     if building in get_buildings_list(db, skip=skip, limit=limit):
#         apartments = get_apartments_list_by_building(db, building=building, skip=skip, limit=limit)
#         return apartments
#     else:raise HTTPException(status_code=404, detail=get_buildings_list(db, skip=skip, limit=limit))
    