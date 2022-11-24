import random
from datetime import date

from faker import Faker

import db.models as models

faker = Faker()


class DataGenerator:
    def __init__(self, db, nrows):
        self.db = db
        self.nrows = nrows

    def generate_data(self):
        self.generate_drivers()
        self.generate_cars()
        self.generate_tickets()

    def generate_drivers(self):
        db_drivers = [
            models.Driver(
                name=faker.first_name(),
                surname=faker.last_name(),
                age=faker.random_int(16, 80),
            )
            for _ in range(self.nrows["drivers"])
        ]
        try:
            self.db.add_all(db_drivers)
            self.db.commit()
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=400, detail=e)
        else:
            return f"{self.nrows['drivers']} drivers generated"

    def generate_cars(self):
        drivers = [d.id for d in self.db.query(models.Driver).all()]
        db_cars = [
            models.Car(
                brand=random.choice(["BMW", "Opel", "Ford", "Fiat", "Toyota"]),
                model=faker.word(),
                year_of_production=faker.random_int(1990, date.today().year),
                mileage=faker.random_int(0, 500000),
                color=random.choice(["white", "black", "red", "silver", "blue"]),
                driver_id=random.choice(drivers),
            )
            for _ in range(self.nrows["cars"])
        ]
        try:
            self.db.add_all(db_cars)
            self.db.commit()
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=400, detail=e)
        else:
            return f"{self.nrows['cars']} cars generated"

    def generate_tickets(self):
        drivers_cars = [(c.driver.id, c.id) for c in self.db.query(models.Car).all()]
        db_tickets = []
        for _ in range(self.nrows["tickets"]):
            driver_car = random.choice(drivers_cars)
            ticket = models.Ticket(
                driver_id=driver_car[0],
                car_id=driver_car[1],
                fine=faker.random_int(50, 5000),
                penalty_points=faker.random_int(1, 10),
            )
            db_tickets.append(ticket)
        try:
            self.db.add_all(db_tickets)
            self.db.commit()
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=400, detail=e)
        else:
            return f"{self.nrows['tickets']} tickets generated"
