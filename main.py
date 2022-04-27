from typing import List
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from app import models
from app.database import engine, SessionLocal
from app.crud import (
    get_comercio,
    list_comercios,
    comercio_create,
    list_empleados,
    get_empleado,
    empleado_create,
    )
from app.schemas import ComercioRequestModel, EmpleadoRequestModel
from app.tools.exceptions import *
from app import create_app


app = create_app()
db = SessionLocal()


@app.on_event("startup")
def startup():
    """This function validates the database connection,
    if the connection is closed, it will open it.
    """
    #create the database tables on app startup or reload
    models.Base.metadata.create_all(bind=engine)
    print(db)
    if not db.is_active:
        print("Opening database connection")
        db.connect()
        print("Creating tables")
        db.create_tables([Comercio])


@app.on_event("shutdown")
def shutdown():
    """This function validates the database connection,
    if the connection is open, it will close it.
    """
    if db.is_active:
        print("Closing database connection")
        db.close()

ListComercios = List[ComercioRequestModel,]

@app.get("/comercios")
def get_list_comercios():
    comercios = list_comercios(db)
    # return object founded
    return {"comercios": comercios}


@app.post("/create_comercio")
def create_comercio(comercio_request: ComercioRequestModel):
    print("comercio_request: ", comercio_request)
    
    comercio = comercio_create(db, comercio_request)
    # return object created
    return {"comercio": comercio}


@app.get("/comercio/{id}")
def get_comercio_by_id(id: int):
    comercio, status = get_comercio(db, id=id)

    if not status:
        return JSONResponse(
            status_code=404,
            content={"rc": comercio.rc, "msg": comercio.msg}
        )
    # return object founded
    return {"comercio": comercio}


@app.get("/empleados")
def get_list_empleados():
    empleados = list_empleados(db)
    
    return {"empleados": empleados}


@app.get("/empleado/{id}")
def get_empleado_by_id(id: int):
    empleado, status = get_empleado(db, id=id)
    
    if not status:
        return JSONResponse(
            status_code=404,
            content={"rc": empleado.rc, "msg": empleado.msg}
        )
    return {"empleado": empleado}


@app.post("/create_empleado")
def create_empleado(empleado_request: EmpleadoRequestModel):
    print("comercio_request: ", empleado_request)
    
    empleado, status = empleado_create(db, empleado_request)

    if not status:
        return JSONResponse(
            status_code=403,
            content={"rc": empleado.rc, "msg": empleado.msg}
        )
    # return object created
    return {"empleado": empleado}