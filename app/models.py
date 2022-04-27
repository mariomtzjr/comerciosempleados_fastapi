import uuid

from sqlalchemy import Column, Integer, String, Boolean, BigInteger
from sqlalchemy.types import DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.schema import UniqueConstraint

from .database import Base


class Comercio(Base):
    __tablename__ = 'comercio'

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String(50), default=uuid.uuid4)
    nombre = Column(String(100), nullable=False)
    activo = Column(Boolean, default=True)
    email_contacto = Column(String(50), nullable=True)
    telefono_contacto = Column(String(15), nullable=True)
    api_key = Column(String(50), nullable=True)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())

    def is_authenticated(self):
        return True
    
    def save(self):
        if not self.pk:
            self.uuid = uuid.uuid4()
        super(Comercio, self).save()


class Empleado(Base):
    __tablename__ = 'empleado'
    # __table_args__ = (
    #     UniqueConstraint('pin', 'comercio', name='unique_pin_comercio'),
    # )

    id = Column(BigInteger, primary_key=True)
    uuid = Column(String(50), default=uuid.uuid4)
    nombre = Column(String(40), nullable=False)
    apellidos = Column(String(40), nullable=False)
    pin = Column(String(6), nullable=False)
    comercio = relationship("Comercio", backref="empleado")
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    activo = Column(Boolean, default=True)

    def save(self):
        if not self.pk:
            self.uuid = uuid.uuid4()
        super(Empleado, self).save()