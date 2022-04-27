from pydantic import BaseModel


class ComercioRequestModel(BaseModel):
    """ ComercioRequestModel
    Determines the structure of the comercio request model,
    the data type that is passed to the endpoint.
    """
    uuid: str
    nombre: str
    activo: bool
    email_contacto: str
    telefono_contacto: str
    api_key: str


class EmpleadoRequestModel(BaseModel):
    """ EmpleadoRequestModel
    Determines the structure of the empleado request model,
    the data type that is passed to the endpoint.
    """
    uuid: str
    nombre: str
    apellidos: str
    pin: str
    comercio_id: int
    activo: bool