from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

import db.models as models
import fastapi_api.schemas as schemas


def create_driver(db: Session, driver: schemas.Driver):
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


def get_drivers(db: Session, limit: int):
    return db.query(models.Driver).limit(limit).all()


def get_driver(db: Session, driver_id: int):
    db_driver = db.query(models.Driver).filter(models.Driver.id == driver_id).first()
    if db_driver is None:
        raise HTTPException(
            status_code=400, detail=f"Driver with id={driver_id} not found"
        )
    return db_driver


def get_driver_cars(db: Session, driver_id: int):
    return db.query(models.Car).filter(models.Car.driver_id == driver_id).all()


def get_driver_tickets(db: Session, driver_id: int):
    return db.query(models.Ticket).filter(models.Ticket.driver_id == driver_id).all()


def create_car(db: Session, car: schemas.Car):
    db_car = models.Car(
        brand=car.brand,
        model=car.model,
        year_of_production=car.year_of_production,
        mileage=car.mileage,
        color=car.color,
        driver_id=car.driver_id,
    )
    try:
        db.add(db_car)
        db.commit()
    except IntegrityError:
        db.rollback()
        error_msg = f"There is no driver with id={car.driver_id}"
        raise HTTPException(status_code=400, detail=error_msg)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=e)
    else:
        return db_car


def create_ticket(db: Session, ticket: schemas.Ticket):
    db_ticket = models.Ticket(
        driver_id=ticket.driver_id,
        car_id=ticket.car_id,
        fine=ticket.fine,
        penalty_points=ticket.penalty_points,
    )
    try:
        db.add(db_ticket)
        db.commit()
        return db_ticket
    except IntegrityError:
        db.rollback()
        error_msg = f"There is no driver with id={ticket.driver_id} or car with id={ticket.car_id}"  # noqa: E501
        raise HTTPException(status_code=400, detail=error_msg)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=e)
    else:
        return db_ticket
