import graphql_api.graphql.schema as schema
import graphql_api.graphql.services as services
import strawberry
from strawberry.types import Info
from config.env import NEW_DATA_NROWS


@strawberry.type
class Mutation:
    @strawberry.mutation
    def generate_data(
        root,
        info: Info,
    ) -> schema.GenerateData:
        db = info.context["db_session"] 
        message = services.generate_data(
            db=db,
            nrows=NEW_DATA_NROWS,
        )
        return schema.MutationResponse(message=message)
       

    @strawberry.mutation
    def create_driver(
        root,
        info: Info,
        name: str,
        surname: str,
        age: int,
    ) -> schema.Driver:
       db = info.context["db_session"] 
       return services.create_driver(
           db=db,
           name=name,
           surname=surname,
           age=age,
       )
    
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
    ) -> schema.Car:
       db = info.context["db_session"] 
       return services.create_car(
            db=db,
            brand=brand,
            model=model,
            year_of_production=year_of_production,
            mileage=mileage,
            color=color,
            driver_id=driver_id,
        )
    
    @strawberry.mutation
    def create_ticket(
        root,
        info: Info,
        driver_id: int,
        car_id: int,
        fine: int,
        penalty_points: int,
    ) -> schema.Ticket:
       db = info.context["db_session"] 
       return services.create_ticket(
           db=db,
           driver_id=driver_id,
           car_id=car_id,
           fine=fine,
           penalty_points=penalty_points,
       )
       

@strawberry.type
class Query:
    pass
