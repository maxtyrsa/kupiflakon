import psycopg2
from db_config import get_db_info
from datetime import datetime

filename='db_info.ini'
section='postgres-sample-db'
db_info = get_db_info(filename,section)

try:
    with psycopg2.connect(**db_info) as db_connection:
        print("Успешно подключено к базе данных.")

        with db_connection.cursor() as db_cursor:
        # Insert one record
                d = datetime.now().strftime('%Y-%m-%d')
                n = input("Номер заказа: ")
                num = (range(0, 100000))
                numb = num[int(n)]
                if numb == 0:
                    numb = None
                p = input("Количество: ")
                print("""
Выберите ТК:
1 - Boxberry
2 - ПЭК
3 - Самовывоз
4 - Деловые линии
5 - Почта России
6 - Yandex Market
7 - Mega Market
8 - AliExpress
9 - Образцы
10 - OZON_FBS
11 - Ярмарка Мастеров
12 - CDEK
13 - WB_FBS
14 - DPD
15 - Бийск
--------------
16 - OZON_FBO
17 - WB_FBO
       """)
                t = int(input("TK: "))
                list_tk = [' ',  'Boxberry', 'ПЭК', 'Самовывоз', 'Деловые линии', 'Почта России', 'Yandex Market', 'Mega Market', 'AliExpress', 'Образцы', 'OZON_FBS', 'Ярмарка Мастеров', 'CDEK', 'WB_FBS', 'DPD', 'Бийск', 'OZON_FBO', 'WB_FBO']
                tk = list_tk[int(t)]
                print("""
Выберите подразделение:
1 - MP
2 - KF
       """)
                b = input("Branch: ")
                company = [' ', 'MP', 'KF']
                branch = company[int(b)]
                insert_record = 'INSERT INTO kupiflakon (date, number, place, t_c, branch) VALUES (%s, %s, %s, %s, %s);'
                insert_value = (d, numb, p, tk, branch)
                db_cursor.execute(insert_record, insert_value)
#except OperationalError:
#    print("Ошибка подключения к базе данных :/")

except (ValueError, NameError, TypeError):
    print("Ошибка ввода данных")

finally:
    if db_connection:
        db_connection.close()
        print("Соединение с PostgreSQL закрыто.")
