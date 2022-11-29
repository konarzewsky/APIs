from sqlalchemy.orm import Session
from db.data_generator import DataGenerator
from graphql import GraphQLError
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
import db.models as models


def generate_data(db: Session, nrows: dict):
    try:
        data_generator = DataGenerator(db=db, nrows=nrows)
        data_generator.generate_data()
        return "Data generated"
    except Exception as e:
        raise GraphQLError


def create_driver(name: str, surname: str, age: int):
    db_driver = models.Driver(
        name=driver.name,
        surname=driver.surname,
        age=driver.age,
    )
    try:
        db.add(db_driver)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=e)
    else:
        return db_driver
