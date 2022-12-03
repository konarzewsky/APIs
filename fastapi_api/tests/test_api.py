from fastapi.testclient import TestClient

import db.models as models
from config.env import API_AUTH_TOKEN, NEW_DATA_NROWS
from db.database import db_session
from fastapi_api.main import app

client = TestClient(app)


headers = {
    "Auth-Token": API_AUTH_TOKEN,
    "Content-Type": "application/json",
}


def test_generate_data():
    response = client.post(
        "/generate_data",
        headers=headers,
    )
    with db_session.begin() as db:
        drivers = db.query(models.Driver).all()
        cars = db.query(models.Car).all()
        tickets = db.query(models.Ticket).all()
    assert response.status_code == 200
    assert len(drivers) == NEW_DATA_NROWS["drivers"]
    assert len(cars) == NEW_DATA_NROWS["cars"]
    assert len(tickets) == NEW_DATA_NROWS["tickets"]


def test_driver():
    response = client.post(
        "/drivers/",
        json={"name": "driver_name", "surname": "driver_surname", "age": 40},
        headers=headers,
    )
    driver = response.json()
    assert response.status_code == 200
    assert driver["name"] == "driver_name"

    response = client.get(
        f"/drivers/{NEW_DATA_NROWS['drivers']+1}",
        headers=headers,
    )
    driver = response.json()
    assert response.status_code == 200
    assert driver["name"] == "driver_name"
    assert driver["surname"] == "driver_surname"


def test_car():
    data = {
        "brand": "car_brand",
        "model": "car_model",
        "year_of_production": 2005,
        "mileage": 175000,
        "color": "brown",
        "driver_id": NEW_DATA_NROWS["drivers"] + 1,
    }
    response = client.post("/cars/", json=data, headers=headers)
    car = response.json()
    assert response.status_code == 200
    assert car["brand"] == "car_brand"

    response = client.get(
        f"/drivers/{NEW_DATA_NROWS['drivers']+1}/cars", headers=headers
    )
    cars = response.json()
    assert response.status_code == 200
    assert cars == [data]


def test_car_invalid_driver_id():
    data = {
        "brand": "car_brand",
        "model": "car_model",
        "year_of_production": 2005,
        "mileage": 175000,
        "color": "brown",
        "driver_id": NEW_DATA_NROWS["drivers"] + 2,
    }
    response = client.post("/cars/", json=data, headers=headers)
    car = response.json()
    assert response.status_code == 400
    assert car["detail"] == f"There is no driver with id={NEW_DATA_NROWS['drivers']+2}"

    response = client.get(
        f"/drivers/{NEW_DATA_NROWS['drivers']+2}/cars", headers=headers
    )
    cars = response.json()
    assert response.status_code == 400
    assert cars["detail"] == f"Driver with id={NEW_DATA_NROWS['drivers']+2} not found"


def test_ticket():
    data = {
        "driver_id": NEW_DATA_NROWS["drivers"] + 1,
        "car_id": 1,
        "fine": 500,
        "penalty_points": 6,
    }
    response = client.post("/tickets/", json=data, headers=headers)
    ticket = response.json()
    assert response.status_code == 200
    assert ticket["fine"] == 500

    response = client.get(
        f"/drivers/{NEW_DATA_NROWS['drivers']+1}/tickets", headers=headers
    )
    tickets = response.json()
    assert response.status_code == 200
    assert tickets == [data]
