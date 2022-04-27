from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app import models
from app.database import engine, SessionLocal
from app.crud import get_comercio, list_comercios


app = FastAPI(
    title="Dapp FastAPI Example",
    description="Dapp FastAPI Example",
    version="1.0.0",
)

#create the database tables on app startup or reload
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/comercio/{id}")
def get_comercio_by_id(db:Session = Depends(get_db), id=int):
    comercio = get_comercio(db=db, id=id)
    # return object founded
    return {"comercio": comercio}

@app.get("/comercios")
def get_list_comercios(db:Session = Depends(get_db)):
    comercios = list_comercios(db=db)
    # return object founded
    return {"comercios": comercios}