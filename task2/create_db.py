from database.model import Base
from database.config import engine

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)