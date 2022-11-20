import os

API_AUTH_TOKEN = os.environ["API_AUTH_TOKEN"]
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")

DB = {
    "DB_HOST": os.environ["DB_HOST"],
    "DB_PORT": os.environ["DB_PORT"],
    "DB_USER": os.environ["DB_USER"],
    "DB_PASSWORD": os.environ["DB_PASSWORD"],
    "DB_NAME": os.environ["DB_NAME"],
}

NEW_DATA_NROWS = {"drivers": 100, "cars": 150, "tickets": 200}
