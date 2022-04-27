from sqlalchemy.orm import Session

"""
Session manages persistence operations for ORM-mapped objects.
Let's just refer to it as a database session for simplicity
"""

from app.models import Comercio


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