import uuid

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, Query

from fastapi import Depends

from .schemas import ComercioRequestModel, EmpleadoRequestModel
from app.models import Comercio, Empleado
from app.tools.exceptions import *


#import crud to give access to the operations that we defined
def comercio_create(db:Session, comercio_request:ComercioRequestModel):
    """
    function to create a friend model object
    """
    data_comercio = comercio_request.dict()
    
    if not data_comercio.get('uuid'):
        data_comercio['uuid'] = str(uuid.uuid4())
    
    if not data_comercio.get('api_key'):
        data_comercio['api_key'] = str(uuid.uuid4())

    # create friend instance 
    new_comercio = Comercio(**data_comercio)
    #place object in the database session
    db.add(new_comercio)
    #commit your instance to the database
    db.commit()
    #reefresh the attributes of the given instance
    db.refresh(new_comercio)
    return new_comercio, True


def get_comercio(db:Session, id:int):
    """
    get the first record with a given id, if no such record exists, will return null
    """
    db_comercio = db.query(Comercio).filter(Comercio.id==id).first()
    return db_comercio


def list_comercios(db:Session):
    """
    Return a list of all existing Comercio records
    """
    all_comercios = db.query(Comercio).all()
    return all_comercios


def list_empleados(db: Session):
    """
    Return a list of all existing Empleado records
    """
    all_empleados = db.query(Empleado).all()
    return all_empleados


def get_empleado(db: Session, id: int):
    """
    get the first record with a given id, if no such record exists, will return null
    """
    db_empleado = db.query(Empleado).filter(Empleado.id==id).first()
    if not db_empleado:
        return InvalidEmpleadoError, False

    return db_empleado, True


def empleado_create(db:Session, empleado_request:EmpleadoRequestModel):
    """
    function to create a empleado model object
    """
    data_empleado = empleado_request.dict()

    try:
        if data_empleado["nombre"] == "" or \
            data_empleado["apellidos"] == "" or \
            data_empleado["pin"] == "":
            
            return IncompleteDataError, False
    except KeyError:
        return IncompleteDataError, False
    

    if not data_empleado.get('uuid'):
        data_empleado['uuid'] = str(uuid.uuid4())

    try:
        # create friend instance 
        new_empleado = Empleado(**data_empleado)
        #place object in the database session
        db.add(new_empleado)
        #commit your instance to the database
        db.commit()
    except IntegrityError:
        return DuplicatedPinError, False

    #reefresh the attributes of the given instance
    db.refresh(new_empleado)
    

    return new_empleado, True