from sqlalchemy import orm

from db.database import db_engine

dbSession = orm.scoped_session(orm.sessionmaker())
dbSession.configure(bind=db_engine)
