import psycopg2
from db_config import get_db_info
import pprint

filename='db_info.ini'
section='postgres-sample-db'
db_info = get_db_info(filename,section)

try:
    with psycopg2.connect(**db_info) as db_connection:
        print("Successfully connected to the database.")
         
        with db_connection.cursor() as db_cursor:
        # Insert one update
            a = int(input("Введите новое количество: "))
            print("""Выберите ТК:
        1 - Boxberry
        2 - ПЭК
        3 - Самовывоз
        4 - Деловые линии
        5 - Почта России
        6 - Yandex Market
        7 - Mega Market
        8 - AliExpress
        9 - Образцы
        10 - OZON
        11 - Ярмарка Мастеров
        12 - CDEK
        13 - Wildberries
        14 - DPD
        15 - Бийск""")
            t = int(input("ТК: "))
            ones = [' ',  'Boxberry', 'ПЭК', 'Самовывоз', 'Деловые линии', 'Почта России', 'Yandex Market', 'Mega Market', 'AliExpress', 'Образцы', 'OZON', 'Ярмарка Мастеров', 'CDEK', 'Wildberries', 'DPD', 'Бийск']
            word = ones[int(t)]
            insert_record = 'UPDATE kupiflakon SET place = %s WHERE date = CURRENT_DATE and t_c = %s;'
            insert_value = (a, word)
            db_cursor.execute(insert_record, insert_value)
except OperationalError:
    print("Error connecting to the database :/")

finally:
    if db_connection:
        db_connection.close()
        print("Запись успешно обновлена.")
