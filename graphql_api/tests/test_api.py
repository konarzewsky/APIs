import db.models as models
from config.env import NEW_DATA_NROWS
from graphql_api.app import schema

pytest_plugins = ["graphql_api.tests.fixtures"]


def test_generate_data(db):
    mutation_generate_data = """
        mutation {
            generateData {
                message
            }
        }
    """
    result = schema.execute_sync(mutation_generate_data, context_value={})
    assert result.errors is None
    assert result.data == {"generateData": {"message": "Data generated"}}
    drivers = db.query(models.Driver).all()
    cars = db.query(models.Car).all()
    tickets = db.query(models.Ticket).all()
    assert len(drivers) == NEW_DATA_NROWS["drivers"]
    assert len(cars) == NEW_DATA_NROWS["cars"]
    assert len(tickets) == NEW_DATA_NROWS["tickets"]


def test_driver():
    mutation_create_driver = """
        mutation {
            createDriver(
                name: "driver_name"
                surname: "driver_surname"
                age: 40
            )
            {
                message
            }
        }
    """
    result = schema.execute_sync(mutation_create_driver, context_value={})
    assert result.errors is None
    assert result.data == {"createDriver": {"message": "Driver created"}}

    query_get_driver = f"""
        query {{
            getDriver(
                driverId: {NEW_DATA_NROWS["drivers"]+1}
            )
            {{
                name
                surname
                age
            }}
        }}
    """
    result = schema.execute_sync(query_get_driver, context_value={})
    assert result.errors is None
    assert result.data == {
        "getDriver": {"name": "driver_name", "surname": "driver_surname", "age": 40}
    }


def test_car():
    mutation_create_car = f"""
        mutation {{
            createCar(
                brand: "car_brand"
                model: "car_model"
                yearOfProduction: 2005
                mileage: 175000
                color: "brown"
                driverId: {NEW_DATA_NROWS["drivers"]+1}
            )
            {{
                message
            }}
        }}
    """
    result = schema.execute_sync(mutation_create_car, context_value={})
    assert result.errors is None
    assert result.data == {"createCar": {"message": "Car created"}}

    query_get_car = f"""
        query {{
            getDriverCars(
                driverId: {NEW_DATA_NROWS["drivers"]+1}
            )
            {{
                brand
                model
            }}
        }}
    """
    result = schema.execute_sync(query_get_car, context_value={})
    assert result.errors is None
    assert result.data == {
        "getDriverCars": [{"brand": "car_brand", "model": "car_model"}]
    }


def test_car_invalid_driver_id():
    mutation_create_car = f"""
        mutation {{
            createCar(
                brand: "car_brand"
                model: "car_model"
                yearOfProduction: 2005
                mileage: 175000
                color: "brown"
                driverId: {NEW_DATA_NROWS["drivers"]+2}
            )
            {{
                message
            }}
        }}
    """
    result = schema.execute_sync(mutation_create_car, context_value={})
    assert (
        result.errors[0].message
        == f"Error while creating Car: There is no driver with id={NEW_DATA_NROWS['drivers']+2}"  # noqa: E501
    )

    query_get_car = f"""
        query {{
            getDriverCars(
                driverId: {NEW_DATA_NROWS["drivers"]+2}
            )
            {{
                brand
                model
            }}
        }}
    """
    result = schema.execute_sync(query_get_car, context_value={})
    assert (
        result.errors[0].message
        == f"Driver with id={NEW_DATA_NROWS['drivers']+2} not found"
    )


def test_ticket():
    mutation_create_ticket = f"""
        mutation {{
            createTicket(
                driverId: {NEW_DATA_NROWS["drivers"]+1}
                carId: 1
                fine: 500
                penaltyPoints: 6
            )
            {{
                message
            }}
        }}
    """
    result = schema.execute_sync(mutation_create_ticket, context_value={})
    assert result.errors is None
    assert result.data == {"createTicket": {"message": "Ticket created"}}

    query_get_ticket = f"""
        query {{
            getDriverTickets(
                driverId: {NEW_DATA_NROWS["drivers"]+1}
            )
            {{
                fine
                penaltyPoints
            }}
        }}
    """
    result = schema.execute_sync(query_get_ticket, context_value={})
    assert result.errors is None
    assert result.data == {"getDriverTickets": [{"fine": 500, "penaltyPoints": 6}]}
