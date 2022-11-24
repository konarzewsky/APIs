from typing import List

from pydantic import BaseModel


class Car(BaseModel):
    brand: str
    model: str
    year_of_production: int
    mileage: int
    color: str
    driver_id: int

    class Config:
        orm_mode = True


class Ticket(BaseModel):
    driver_id: int
    car_id: int
    fine: int
    penalty_points: int

    class Config:
        orm_mode = True


class Driver(BaseModel):
    name: str
    surname: str
    age: int
    car: List[Car]
    ticket: List[Ticket]

    class Config:
        orm_mode = True
