from sqlalchemy import select

from .config import Base, Session


class TradingDao():
    def __init__(self, model: Base):
        self.model = model

    def insert_data(self, data: dict):
        with Session() as session:
            session.add(data)
            session.commit()

    def insert_all_data(self, data: list[dict]):
        mappings = [item.model_dump() for item in data]
        with Session() as session:
            session.bulk_insert_mappings(self.model, mappings)
            session.commit()

    def fetch_data(self):
        with Session() as session:
            query = select(self.model)
            model_db = session.execute(query)
            return model_db
