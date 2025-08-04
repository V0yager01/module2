from datetime import date, datetime

from database.shemas import TradingShema
from database.dao import TradingDao
from database.model import Trading
from parsers.request_parser import pageparser
from parsers.xls_parser import pandas_module
from parsers.load_xls import load_xls_bytes


from const import URL, NEXT_PAGE_URL, PAGE_COUNTS

xls_links = []

def client_code():
    # Создание списка ссылок на таблицы
    trading_unit = TradingDao(model=Trading)
    xls_links = []
    xls = pageparser.XlsParserService(pageparser.ParserPageLinks())
    for i in range(1, PAGE_COUNTS+1):
        result = xls.parse_page(url=URL, next_page=NEXT_PAGE_URL,
                                page_number=i,
                                start_date=date(year=2023, month=1, day=1),
                                end_date=date.today())
        if result:
            xls_links = xls_links + result
        else:
            break
    count_of_xls = len(xls_links)
    counter = 1

    # Загрузка таблиц, парсинг таблиц, добавление в бд.
    for index in range(len(xls_links)):
        try:
            # Загрузка таблицы
            xls_bytes = load_xls_bytes(xls_links[index][0])
            # Парсинг таблицы
            parsed_xls = pandas_module.parse_xls(xls_bytes)
            to_db = []
            for _, row in parsed_xls.iterrows():
                xls_model = TradingShema(
                    exchange_product_id=str(row['Код Инструмента']),
                    exchange_product_name=str(row['Наименование Инструмента']),
                    delivery_basis_name=str(row['Базис поставки']),
                    volume=float(row['Объем Договоров в единицах измерения']),
                    total=int(row['Обьем Договоров, руб.']),
                    count=int(row['Количество Договоров, шт.']),
                    oil_id=str(row['Код Инструмента'][:4]),
                    delivery_basis_id=str(row['Код Инструмента'][4:7]),
                    delivery_type_id=str(row['Код Инструмента'][-1]),
                    date=xls_links[index][1],
                    created_on=datetime.now(),
                    updated_on=datetime.now()
                )
                if xls_model:
                    to_db.append(xls_model)
            # Добавление в бд
            trading_unit.insert_all_data(to_db)
            print(f'Progress: {counter}/{count_of_xls}')
            counter += 1
        except Exception as e:
            print(e)


if __name__ == "__main__":
    client_code()