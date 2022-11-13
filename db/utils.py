from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.env import DB


def get_postgres_uri(db: dict) -> str:
    return f"postgresql://{DB['DB_USER']}:{DB['DB_PASSWORD']}@{DB['DB_HOST']}:{DB['DB_PORT']}/{DB['DB_NAME']}"

DB_URI = get_postgres_uri(DB)
db_engine = create_engine(DB_URI)
get_db_session = sessionmaker(bind=db_engine)
