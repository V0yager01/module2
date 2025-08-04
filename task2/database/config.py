from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, DeclarativeBase


from loader import(DB_HOST, DB_PORT, DB_USER, DB_NAME, DB_PASSWORD)

POSTGRESS_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(url=POSTGRESS_URL)

Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass
