from typing import List, Optional

import strawberry
from strawberry.types import Info

import graphql_api.graphql.schema as schema
import graphql_api.graphql.services as services


@strawberry.type
class Query:
    @strawberry.field
    def get_drivers(root, info: Info, limit: int) -> Optional[List[schema.DriverType]]:
        db = info.context["db_session"]
        drivers = services.get_drivers(db=db, limit=limit)
        return [schema.DriverType.from_orm(driver) for driver in drivers]

    @strawberry.field
    def get_driver(root, info: Info, driver_id: int) -> Optional[schema.DriverType]:
        db = info.context["db_session"]
        driver = services.get_object(db=db, type="Driver", driver_id=driver_id)
        return schema.DriverType.from_orm(driver) if driver else None

    @strawberry.field
    def get_driver_cars(
        root, info: Info, driver_id: int
    ) -> Optional[List[schema.CarType]]:
        db = info.context["db_session"]
        cars = services.get_object(db=db, type="Car", driver_id=driver_id)
        return [schema.CarType.from_orm(car) for car in cars]  # type: ignore

    @strawberry.field
    def get_driver_tickets(
        root, info: Info, driver_id: int
    ) -> Optional[List[schema.TicketType]]:
        db = info.context["db_session"]
        tickets = services.get_object(db=db, type="Ticket", driver_id=driver_id)
        return [schema.TicketType.from_orm(ticket) for ticket in tickets]  # type: ignore
