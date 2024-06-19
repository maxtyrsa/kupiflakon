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
            db_cursor.execute("SELECT * FROM kupiflakon WHERE date = CURRENT_DATE;")
            x = db_cursor.fetchall()
            print(str(x).replace('), (', '\n'))
        # Insert one record
            a = int(input("Введите id: "))
            b = int(input("Введите сумму: "))
            insert_record = 'INSERT INTO money (id, amount) VALUES (%s, %s);'
            insert_value = (a, b)
            db_cursor.execute(insert_record, insert_value)
except OperationalError:
    print("Error connecting to the database :/")

finally:
    if db_connection:
        db_connection.close()
        print("Запись успешно добавлена.")
