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
                n = int(input("Введите номер заказа: "))
                db_cursor.execute('SELECT * FROM kupiflakon WHERE number = %s;', (n,))
                print(db_cursor.fetchone())
        # Insert one record
                i = input("Введите id: ")
                p = input("Количество мест: ")
                d = datetime.now().strftime('%Y-%m-%d')
                print("""Выберите статус:
1 - Повтор
2 - Обмен
3 - Возврат
   """)
                j = int(input("Статус: "))
                ones = [' ',  'Ошибка', 'Недовложение', 'Лишнее']
                word = ones[int(j)]
                insert_record = 'INSERT INTO repeated (id, repeat, place, date) VALUES (%s, %s, %s, %s);'
                insert_value = (i, word, p, d)
                db_cursor.execute(insert_record, insert_value)
#except OperationalError:
#    print("Ошибка подключения к базе данных :/")
except (ValueError, NameError, TypeError):
    print("Ошибка ввода данных")


finally:
    if db_connection:
        db_connection.close()
        print("Соединение с PostgreSQL закрыто.")
