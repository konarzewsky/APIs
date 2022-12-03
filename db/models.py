from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from db.database import Base


class Driver(Base):
    __tablename__ = "drivers"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())

    car = relationship("Car", back_populates="driver")
    ticket = relationship("Ticket", back_populates="driver")


class Car(Base):
    __tablename__ = "cars"

    id = Column(BigInteger, primary_key=True, index=True)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year_of_production = Column(Integer, nullable=False)
    mileage = Column(Integer, nullable=False)
    color = Column(String, nullable=False)
    driver_id = Column(Integer, ForeignKey("drivers.id"), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())

    driver = relationship("Driver", back_populates="car")
    ticket = relationship("Ticket", back_populates="car")


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(BigInteger, primary_key=True, index=True)
    driver_id = Column(Integer, ForeignKey("drivers.id"), nullable=False)
    car_id = Column(Integer, ForeignKey("cars.id"))
    fine = Column(Integer)
    penalty_points = Column(Integer)
    created_at = Column(DateTime, nullable=False, server_default=func.now())

    car = relationship("Car", back_populates="ticket")
    driver = relationship("Driver", back_populates="ticket")
