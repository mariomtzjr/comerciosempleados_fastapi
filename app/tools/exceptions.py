import uuid

from app.database import Base


class BaseError(Exception):
    rc = -1000
    msg = "Error"


class NoEmpleadoError(BaseError):
    rc = -1001
    msg = "Please enter a valid id"


class InvalidEmpleadoError(BaseError):
    rc = -1002
    msg = "Invalid id"


class DuplicatedPinError(BaseError):
    rc = -1003
    msg = "Duplicated PIN"


class IncompleteDataError(BaseError):
    rc = -1004
    msg = "Incomplete data"


class NoComercioError(BaseError):
    rc = -1005
    msg = "Comercio not found"


class AuthenticationFailedError(BaseError):
    rc = 401
    msg = "API key is not valid"