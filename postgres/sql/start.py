import psycopg2
import pandas as pd

# Connection parameters, yours will be different
param_dic = {
    "host"      : "pg3.sweb.ru",
    "database"  : "tyrsadocto",
    "user"      : "tyrsadocto",
    "password"  : "T5p2fga5c8y"
}
try:
    with psycopg2.connect(**param_dic) as db_connection:
        print("Успешно подключено к базе данных.")
        with db_connection.cursor() as db_cursor:
            db_cursor.execute("SELECT id, number, t_c FROM kupiflakon WHERE date = CURRENT_DATE;")
            #x = db_cursor.fetchall()
            #print(str(x).replace('), (', '\n'))
        a = int(input("Введите id: "))
               # b = int(input("Введите сумму заказа: "))
               # d = int(input("Введите сумму доставки: "))
        db_cursor.execute('INSERT INTO time_start (id, time) VALUES (%s, CURRENT_TIMESTAMP)', [a]);
except (ValueError, NameError, TypeError):
    print("Ошибка ввода данных")
finally:
    if db_connection:
        db_connection.close()
        print("Соединение с PostgreSQL закрыто.")
