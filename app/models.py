import uuid

from sqlalchemy import Column, Integer, String, Boolean, BigInteger, ForeignKey, UniqueConstraint
from sqlalchemy.types import DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from .database import Base


class Comercio(Base):
    __tablename__ = 'comercio'

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String(50), default='')
    nombre = Column(String(100), nullable=False)
    activo = Column(Boolean, default=True)
    email_contacto = Column(String(50), nullable=True)
    telefono_contacto = Column(String(15), nullable=True)
    api_key = Column(String(50), nullable=True)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())

    def is_authenticated(self):
        return True


class Empleado(Base):
    __tablename__ = 'empleado'
    __table_args__ = (
        UniqueConstraint('pin', 'comercio_id', name='unique_pin_comercio'),
    )

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String(50), default='')
    nombre = Column(String(40), nullable=False)
    apellidos = Column(String(40), nullable=False)
    pin = Column(String(6), nullable=False, unique=True)
    comercio_id = Column(Integer, ForeignKey("comercio.id"), nullable=False)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    activo = Column(Boolean, default=True)

    comercio = relationship("Comercio", cascade="all, delete")