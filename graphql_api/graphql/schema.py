from datetime import datetime

import strawberry


@strawberry.type
class DriverType:
    name: str
    surname: str
    age: int
    created_at: datetime


@strawberry.type
class CarType:
    brand: str
    model: str
    year_of_production: int
    mileage: int
    color: str
    driver: DriverType
    created_at: datetime


@strawberry.type
class TicketType:
    driver: DriverType
    car: CarType
    fine: int | None
    penalty_points: int | None


@strawberry.type
class Message:
    message: str
