from typing import List, Literal, Optional, Union

from graphql import GraphQLError
from sqlalchemy.exc import SQLAlchemyError
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
    except SQLAlchemyError as e:
        db.rollback()
        raise GraphQLError(f"Error while creating {type}: {e}")
    else:
        return f"{type} created"


def get_drivers(db: Session, limit: int = 100):
    return db.query(models.Driver).limit(limit).all()


def get_object(
    db: Session, type: Literal["Driver", "Car", "Ticket"], driver_id: int
) -> Union[Optional[models.Driver], List[models.Car], List[models.Ticket]]:
    if type == "Driver":
        return db.query(models.Driver).filter(models.Driver.id == driver_id).first()
    else:
        return (
            db.query(getattr(models, type))
            .filter(getattr(models, type).driver_id == driver_id)
            .all()
        )
