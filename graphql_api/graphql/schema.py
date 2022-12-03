from datetime import datetime
from typing import Optional

import strawberry

import db.models as models


@strawberry.type
class DriverType:
    name: str
    surname: str
    age: int
    created_at: datetime

    @classmethod
    def from_orm(cls, driver: models.Driver):
        return DriverType(
            name=driver.name,
            surname=driver.surname,
            age=driver.age,
            created_at=driver.created_at,
        )


@strawberry.type
class CarType:
    brand: str
    model: str
    year_of_production: int
    mileage: int
    color: str
    driver: DriverType
    created_at: datetime

    @classmethod
    def from_orm(cls, car: models.Car):
        return CarType(
            brand=car.brand,
            model=car.model,
            year_of_production=car.year_of_production,
            mileage=car.mileage,
            color=car.color,
            driver=car.driver,
            created_at=car.created_at,
        )


@strawberry.type
class TicketType:
    driver: DriverType
    car: CarType
    fine: Optional[int]
    penalty_points: Optional[int]

    @classmethod
    def from_orm(cls, ticket: models.Ticket):
        return TicketType(
            driver=ticket.driver,
            car=ticket.car,
            fine=ticket.fine,
            penalty_points=ticket.penalty_points,
        )


@strawberry.type
class Message:
    message: str
