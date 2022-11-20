from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

import fastapi_api.crud as crud
from config.env import NEW_DATA_NROWS
from db.data_generator import DataGenerator
from fastapi_api.dependencies import get_db_conn, verify_auth_token
from fastapi_api.schemas import Car, Driver, Ticket

app = FastAPI(dependencies=[Depends(verify_auth_token)])


@app.get("/")
def root():
    return {"message": "FastAPI api - Welcome!"}


@app.post("/generate_data")
def generate_data(db: Session = Depends(get_db_conn)):
    data_generator = DataGenerator(db=db, nrows=NEW_DATA_NROWS)
    data_generator.generate_data()
    return {"message": "Data generated"}


@app.post("/drivers/", response_model=Driver)
def create_driver(driver: Driver, db: Session = Depends(get_db_conn)):
    return crud.create_driver(db=db, driver=driver)


@app.get("/drivers/", response_model=List[Driver])
def get_drivers(limit: int = 100, db: Session = Depends(get_db_conn)):
    return crud.get_drivers(db=db, limit=limit)


@app.get("/drivers/{driver_id}", response_model=Driver)
def get_driver(driver_id: int, db: Session = Depends(get_db_conn)):
    return crud.get_driver(db=db, driver_id=driver_id)


@app.get("/drivers/{driver_id}/cars", response_model=List[Car])
def get_driver_cars(driver_id: int, db: Session = Depends(get_db_conn)):
    crud.get_driver(db=db, driver_id=driver_id)
    return crud.get_driver_cars(db=db, driver_id=driver_id)


@app.get("/drivers/{driver_id}/tickets", response_model=List[Ticket])
def get_driver_tickets(driver_id: int, db: Session = Depends(get_db_conn)):
    crud.get_driver(db=db, driver_id=driver_id)
    return crud.get_driver_tickets(db=db, driver_id=driver_id)


@app.post("/cars/", response_model=Car)
def create_car(car: Car, db: Session = Depends(get_db_conn)):
    return crud.create_car(db=db, car=car)


@app.post("/tickets/", response_model=Ticket)
def create_ticket(ticket: Ticket, db: Session = Depends(get_db_conn)):
    return crud.create_ticket(db=db, ticket=ticket)
