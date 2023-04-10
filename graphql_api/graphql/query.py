import strawberry
from strawberry.types import Info

import graphql_api.graphql.schema as schema
import graphql_api.graphql.services as services


@strawberry.type
class Query:
    @strawberry.field
    def get_drivers(root, info: Info, limit: int) -> list[schema.DriverType]:
        db = info.context["db_session"]
        drivers = services.get_drivers(db=db, limit=limit)
        return drivers  # type: ignore

    @strawberry.field
    def get_driver(root, info: Info, driver_id: int) -> schema.DriverType | None:
        db = info.context["db_session"]
        driver = services.get_object(db=db, type="Driver", driver_id=driver_id)
        return driver  # type: ignore

    @strawberry.field
    def get_driver_cars(
        root, info: Info, driver_id: int
    ) -> list[schema.CarType] | None:
        db = info.context["db_session"]
        cars = services.get_object(db=db, type="Car", driver_id=driver_id)
        return cars  # type: ignore

    @strawberry.field
    def get_driver_tickets(
        root, info: Info, driver_id: int
    ) -> list[schema.TicketType] | None:
        db = info.context["db_session"]
        tickets = services.get_object(db=db, type="Ticket", driver_id=driver_id)
        return tickets  # type: ignore
