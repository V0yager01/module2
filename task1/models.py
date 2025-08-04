from datetime import date

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, ForeignKey, Date, Float

from main import Base


class Genre(Base):
    __tablename__ = "genre"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    genre_name: Mapped[str]


class Author(Base):
    __tablename__ = "author"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_name: Mapped[str] = mapped_column(String)


class City(Base):
    __tablename__ = 'city'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    city_name: Mapped[str] = mapped_column(String)
    days_delivery: Mapped[date] = mapped_column(Date)


class Book(Base):
    __tablename__ = 'book'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String)
    author_id: Mapped[int] = mapped_column(ForeignKey('author.id'))
    genre_id: Mapped[int] = mapped_column(ForeignKey('genre.id'))
    price: Mapped[float] = mapped_column(Float)
    amount: Mapped[int] = mapped_column(Integer) 


class Client(Base):
    __tablename__ = 'client'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    client_name: Mapped[str] = mapped_column(String)
    city_id: Mapped[int] = mapped_column(ForeignKey('city.id'))
    email: Mapped[str] = mapped_column(String)


class Buy(Base):
    __tablename__ = 'buy'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    buy_descriptions: Mapped[str] = mapped_column(String)
    cliend_id: Mapped[int] = mapped_column(ForeignKey('client.id'))


class Step(Base):
    __tablename__ = 'step'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name_step: Mapped[str] = mapped_column(String)


class Buy_Book(Base):
    __tablename__ = 'buy_book'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    buy_id: Mapped[int] = mapped_column(ForeignKey('buy.id'))
    book_id: Mapped[int] = mapped_column(ForeignKey('book.id'))
    amount: Mapped[int] = mapped_column(Integer)


class Buy_Step(Base):
    __tablename__ = 'buy_step'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    buy_id: Mapped[int] = mapped_column(ForeignKey('buy.id'))
    step_id: Mapped[int] = mapped_column(ForeignKey('step.id'))
    date_step_beg: Mapped[date] = mapped_column(Date)
    date_step_end: Mapped[date] = mapped_column(Date)
