import strawberry
from typing import Optional
import db.models as models
from datetime import datetime


@strawberry.type
class DriverType:
    id: strawberry.ID
    name: str
    surname: str
    age: int
    created_at: datetime

    @classmethod
    def from_orm(cls, driver: models.Driver):
        return DriverType(
            id=driver.id,
            name=driver.name,
            surname=driver.surname,
            age=driver.age,
            created_at = driver.created_at
        )


@strawberry.type
class CarType:
    id: strawberry.ID
    brand: str
    model: str
    year_of_production: int
    mileage: int
    color: str
    driver: Driver
    created_at: datetime
    
    @classmethod
    def from_orm(cls, car: models.Car):
        return CarType(
            id=car.id,
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
    id: strawberry.ID
    driver: Driver
    car: Car
    fine: Optional[int]
    penalty_points: Optional[int]

    @classmethod
    def from_orm(cls, ticket: models.Ticket):
        return TicketType(
            id=ticket.id,
            driver=ticket.driver,
            car=ticket.car,
            fine=ticket.fine,
            penalty_points=ticket.penalty_points,
        )


@strawberry.type
class Message:
    message: str
