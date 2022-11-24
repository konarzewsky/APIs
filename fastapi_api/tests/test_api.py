from fastapi.testclient import TestClient

import db.models as models
from config.env import API_AUTH_TOKEN, NEW_DATA_NROWS
from db.database import db_session
from fastapi_api.main import app

client = TestClient(app)


def test_generating_data():
    response = client.post(
        "/generate_data",
        headers={
            "Auth-Token": API_AUTH_TOKEN,
            "Content-Type": "application/json",
        },
    )
    with db_session.begin() as db:
        drivers = db.query(models.Driver).all()
        cars = db.query(models.Car).all()
        tickets = db.query(models.Ticket).all()

    assert response.status_code == 200
    assert len(drivers) == NEW_DATA_NROWS["drivers"]
    assert len(cars) == NEW_DATA_NROWS["cars"]
    assert len(tickets) == NEW_DATA_NROWS["tickets"]
