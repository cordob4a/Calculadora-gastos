from sqlalchemy import Column, Integer, String, Date, Float
from app.db.database import Base

class Gasto(Base):
    __tablename__ = "gastos"

    id = Column(Integer, primary_key=True, index=True)
    gasto = Column(String, nullable=False)
    monto = Column(Float, nullable=False)
    fecha = Column(Date, nullable=False)
    descripcion = Column(String, nullable=False)
