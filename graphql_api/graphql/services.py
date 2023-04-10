from typing import Literal

from graphql import GraphQLError
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

import db.models as models
from db.data_generator import DataGenerator


def generate_data(db: Session, nrows: dict) -> str:
    try:
        data_generator = DataGenerator(db=db, nrows=nrows)
        data_generator.generate_data()
        return "Data generated"
    except Exception as e:
        raise GraphQLError(f"Error while generating data: {e}")


def create_object(
    type: Literal["Driver", "Car", "Ticket"], db: Session, **kwargs
) -> str:
    db_object = getattr(models, type)(**kwargs)
    try:
        db.add(db_object)
        db.commit()
    except IntegrityError as e:
        db.rollback()
        if type == "Car":
            e = f"There is no driver with id={kwargs.get('driver_id')}"
        elif type == "Ticket":
            e = f"There is no driver with id={kwargs.get('driver_id')} or car with id={kwargs.get('car_id')}"  # noqa: E501
        raise GraphQLError(f"Error while creating {type}: {e}")
    except SQLAlchemyError as e:
        db.rollback()
        raise GraphQLError(f"Error while creating {type}: {e}")
    else:
        return f"{type} created"


def get_drivers(db: Session, limit: int = 100) -> list[models.Driver]:
    return db.query(models.Driver).limit(limit).all()


def get_object(
    db: Session, type: Literal["Driver", "Car", "Ticket"], driver_id: int
) -> models.Driver | list[models.Car] | list[models.Ticket] | None:
    driver = db.query(models.Driver).filter(models.Driver.id == driver_id).first()
    if not driver:
        raise GraphQLError(f"Driver with id={driver_id} not found")
    if type == "Driver":
        return driver
    else:
        return (
            db.query(getattr(models, type))
            .filter(getattr(models, type).driver_id == driver_id)
            .all()
        )
