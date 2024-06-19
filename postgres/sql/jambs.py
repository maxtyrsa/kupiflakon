import psycopg2
from db_config import get_db_info
from datetime import datetime

filename='db_info.ini'
section='postgres-sample-db'
db_info = get_db_info(filename,section)

try:
    with psycopg2.connect(**db_info) as db_connection:
        print("Successfully connected to the database.")
         
        with db_connection.cursor() as db_cursor:
                n = int(input("Введите номер заказа: "))
                db_cursor.execute('SELECT * FROM kupiflakon WHERE number = %s;', (n,))
                print(db_cursor.fetchone())
        # Insert one record
                i = input("Введите id: ")
                p = input("Количество мест: ")
                d = datetime.now().strftime('%Y-%m-%d')
                print("""Выберите статус:
1 - Ошибка
2 - Недовложение
3 - Лишнее
""")
                j = int(input("Статус: "))
                ones = [' ',  'Ошибка', 'Недовложение', 'Лишнее']
                word = ones[int(j)]
                insert_record = 'INSERT INTO jambs (id, jamb, place, date) VALUES (%s, %s, %s, %s);'
                insert_value = (i, word, p, d)
                db_cursor.execute(insert_record, insert_value)
except OperationalError:
    print("Error connecting to the database :/")

finally:
    if db_connection:
        db_connection.close()
        print("Запись успешно добавлена.")
