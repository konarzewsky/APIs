import strawberry
from strawberry.types import Info

import graphql_api.graphql.schema as schema
import graphql_api.graphql.services as services
from config.env import NEW_DATA_NROWS


@strawberry.type
class Mutation:
    @strawberry.mutation
    def generate_data(
        root,
        info: Info,
    ) -> schema.Message:
        db = info.context["db_session"]
        message = services.generate_data(
            db=db,
            nrows=NEW_DATA_NROWS,
        )
        return schema.Message(message=message)

    @strawberry.mutation
    def create_driver(
        root,
        info: Info,
        name: str,
        surname: str,
        age: int,
    ) -> schema.Message:
        db = info.context["db_session"]
        message = services.create_object(
            type="Driver",
            db=db,
            name=name,
            surname=surname,
            age=age,
        )
        return schema.Message(message=message)

    @strawberry.mutation
    def create_car(
        root,
        info: Info,
        brand: str,
        model: str,
        year_of_production: int,
        mileage: int,
        color: str,
        driver_id: int,
    ) -> schema.Message:
        db = info.context["db_session"]
        message = services.create_object(
            type="Car",
            db=db,
            brand=brand,
            model=model,
            year_of_production=year_of_production,
            mileage=mileage,
            color=color,
            driver_id=driver_id,
        )
        return schema.Message(message=message)

    @strawberry.mutation
    def create_ticket(
        root,
        info: Info,
        driver_id: int,
        car_id: int,
        fine: int,
        penalty_points: int,
    ) -> schema.Message:
        db = info.context["db_session"]
        message = services.create_object(
            type="Ticket",
            db=db,
            driver_id=driver_id,
            car_id=car_id,
            fine=fine,
            penalty_points=penalty_points,
        )
        return schema.Message(message=message)
