from typing import Literal

from graphql import GraphQLError
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

import db.models as models
from db.data_generator import DataGenerator


def generate_data(db: Session, nrows: dict):
    try:
        data_generator = DataGenerator(db=db, nrows=nrows)
        data_generator.generate_data()
        return "Data generated"
    except Exception as e:
        raise GraphQLError(f"Error while generating data: {e}")


def create_object(type: Literal["Driver", "Car", "Ticket"], db: Session, **kwargs):
    db_object = getattr(models, type)(**kwargs)
    try:
        db.add(db_object)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise GraphQLError(f"Error while creating {type}: {e}")
    else:
        return f"{type} created"
