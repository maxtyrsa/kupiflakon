import psycopg2
import pandas as pd
import configparser
from datetime import datetime
from rich.table import Table
from rich.console import Console
import numpy as np

# Общие настройки и функции
param_dict = {
    "host": "pg3.sweb.ru",
    "database": "tyrsadocto",
    "user": "tyrsadocto",
    "password": "T5p2fga5c8y"
}

def get_db_info(filename, section):
    parser = configparser.ConfigParser()
    parser.read(filename)
    db_info = {}
    if parser.has_section(section):
        key_val_tuple = parser.items(section)
        for item in key_val_tuple:
            db_info[item[0]] = item[1]
    return db_info

def connect(params_dict):
    conn = None
    try:
        print("Подключение к базе данных PostgreSQL...")
        conn = psycopg2.connect(**params_dict)
        print("Подключение прошло успешно!")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Ошибка: {error}")
        return None
    return conn


def postgresql_to_dataframe(conn, select_query, column_names):
    cursor = conn.cursor()
    try:
        cursor.execute(select_query)
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Ошибка: {error}")
        cursor.close()
        return None
    tuples = cursor.fetchall()
    cursor.close()
    df = pd.DataFrame(tuples, columns=column_names)
    return df

# Функции из отдельных скриптов
def number_search():
    try:
        conn = connect(param_dict)
        if conn is None:
            return
        column_names = ["id", "Дата", "Номер заказа", "Места", "ТК", "Подразделение"]
        n = int(input("Введите номер заказа: "))
        df = postgresql_to_dataframe(conn, f"SELECT * FROM kupiflakon WHERE number = {n}", column_names)
        if df is None or len(df) == 0:
            print("Нет данных")
        else:
            print(df.query('number == @n'))
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
      if conn:
        conn.close()


def orders_today():
    try:
        conn = connect(param_dict)
        if conn is None:
            return
        column_names = ["id", "Дата", "Номер заказа", "Места", "ТК", "Подразделение"]
        k = int(input("Количество с конца: "))
        df = postgresql_to_dataframe(conn, "SELECT * FROM kupiflakon WHERE date = CURRENT_DATE", column_names)
        if df is None:
            print("Нет данных")
            return
        if len(df) > 30:
          print(df.tail(k))
        elif len(df) > 0:
            print(df.tail(k))
        else:
            print("Нет данных")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
      if conn:
        conn.close()

def time_end():
    try:
        conn = connect(param_dict)
        if conn is None:
            return
        with conn.cursor() as db_cursor:
          db_cursor.execute("SELECT id, number, t_c FROM kupiflakon WHERE date = CURRENT_DATE")
          #print(str(db_cursor.fetchall()).replace('), (', ',\n'))
          a = int(input("Введите id: "))
          db_cursor.execute("INSERT INTO time_end (id, time) VALUES (%s, CURRENT_TIMESTAMP)", [a])
        conn.commit()
        print("Успешная вставка в time_end")
    except Exception as e:
      print(f"Ошибка ввода данных: {e}")
      conn.rollback()
    finally:
      if conn:
        conn.close()

def time_start():
    try:
      conn = connect(param_dict)
      if conn is None:
            return
      with conn.cursor() as db_cursor:
        db_cursor.execute("SELECT id, number, t_c FROM kupiflakon WHERE date = CURRENT_DATE")
        #print(str(db_cursor.fetchall()).replace('), (', ',\n'))
        a = int(input("Введите id: "))
        db_cursor.execute("INSERT INTO time_start (id, time) VALUES (%s, CURRENT_TIMESTAMP)", [a])
      conn.commit()
      print("Успешная вставка в time_start")
    except Exception as e:
      print(f"Ошибка ввода данных: {e}")
      conn.rollback()
    finally:
        if conn:
            conn.close()

def money_records():
  filename = 'db_info.ini'
  section = 'postgres-sample-db'
  db_info = get_db_info(filename, section)

  try:
    with psycopg2.connect(**db_info) as db_connection:
        with db_connection.cursor() as db_cursor:
            db_cursor.execute("SELECT id, number, t_c FROM kupiflakon WHERE date = CURRENT_DATE")
            x = db_cursor.fetchall()
            print(str(x).replace('), (', ',\n'))

            x = int(input("Введите количество заказов: "))
            for i in range(x):
              a = int(input("Введите id: "))
              b = int(input("Введите сумму заказа: "))
              d = int(input("Введите сумму доставки: "))
              insert_record = 'INSERT INTO money (id, amount) VALUES (%s, %s)'
              insert_value = (a, b - d)
              db_cursor.execute(insert_record, insert_value)
        db_connection.commit()
        print("Успешная вставка в money")
  except Exception as e:
    print(f"Ошибка ввода данных: {e}")
  finally:
    if db_connection:
      db_connection.close()

def kupiflakon_insert():
    filename = 'db_info.ini'
    section = 'postgres-sample-db'
    db_info = get_db_info(filename, section)

    try:
        with psycopg2.connect(**db_info) as db_connection:
            with db_connection.cursor() as db_cursor:
                x = int(input("Введите количество заказов: "))
                for i in range(x):
                    date_str = datetime.now().strftime('%Y-%m-%d')
                    n = input("Номер заказа: ")
                    if n == "":
                       n = None
                    else:
                      n = int(n)
                    num = int(input('Количество: '))
                    if num == "":
                      num = None
                    else:
                      num = str(num).zfill(5)
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
                    list_tk = [
    'Boxberry', 'ПЭК', 'Самовывоз', 'Деловые линии', 
    'Почта России', 'Yandex Market', 'Mega Market', 
    'AliExpress', 'Образцы', 'OZON_FBS', 'Ярмарка Мастеров', 
    'CDEK', 'WB_FBS', 'DPD', 'Бийск', 'OZON_FBO', 'WB_FBO'
                    ]
                    tk = int(input("TK: "))
                    tk = list_tk[tk-1]
                    print("""
Выберите подразделение:
    1 - Маркетплейс
    2 - Купи-Флакон
    3 - Pack Stage
    ----
    """)
                    list_branch = [
                        'MP', 'KF', 'Pack Stage'
                    ]
                    b = int(input("Branch: "))
                    company = list_branch[b-1]
                    
                    insert_record = 'INSERT INTO kupiflakon (date, number, place, t_c, branch) VALUES (%s, %s, %s, %s, %s)'
                    insert_value = (date_str, n, num, tk, company)
                    db_cursor.execute(insert_record, insert_value)
            db_connection.commit()
            print("Успешная вставка в kupiflakon")
    except Exception as e:
        print(f"Ошибка ввода данных: {e}")
        db_connection.rollback()
    finally:
      if db_connection:
            db_connection.close()

def info_order():
    try:
        conn = connect(param_dict)
        if conn is None:
            return
        column_names = ["id", "Дата", "Номер заказа", "Места","Сумма","ТК", "Подразделение"]
        date_start = input("Введите начальную дату в формате ГГГГ-ММ-ДД: ")
        year_s, month_s, day_s = [int(item) for item in date_start.split('-')]
        date_start = datetime(year_s, month_s, day_s)
        
        date_end = input("Введите конечную дату в формате ГГГГ-ММ-ДД (если нужен один день нажмите enter): ")
        if date_end:
          year_e, month_e, day_e = [int(item) for item in date_end.split('-')]
          date_end = datetime(year_e, month_e, day_e)
          df = postgresql_to_dataframe(conn, f"SELECT k.id, k.date, k.number, k.place, m.amount, k.t_c, k.branch FROM kupiflakon k LEFT JOIN money m ON k.id = m.id WHERE k.date BETWEEN '{date_start}' AND '{date_end}'", column_names)
        else:
           df = postgresql_to_dataframe(conn, f"SELECT k.id, k.date, k.number, k.place, m.amount, k.t_c, k.branch FROM kupiflakon k LEFT JOIN money m ON k.id = m.id WHERE k.date = '{date_start}'", column_names)
        if df is None:
            print("No data")
            return
        print('Итого:' ,df.amount.sum(), '₽')
        print('Количество заказов:', df.place.shape[0], 'шт')
        print('Сумма в среднем за один заказ:', round(np.mean(df.amount)), '₽')
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        if conn:
            conn.close()

def update_kupiflakon():
  filename = 'db_info.ini'
  section = 'postgres-sample-db'
  db_info = get_db_info(filename, section)

  try:
    with psycopg2.connect(**db_info) as db_connection:
      with db_connection.cursor() as db_cursor:
          db_cursor.execute("SELECT * FROM kupiflakon WHERE date = CURRENT_DATE;")
          print(str(db_cursor.fetchall()).replace('), (', ',\n'))
          
          i = int(input("Введите id: "))
          a = int(input("Введите новое количество: "))
          db_cursor.execute("UPDATE kupiflakon SET place = %s WHERE date = CURRENT_DATE AND id = %s;", (a, i))
      db_connection.commit()
      print("Успешная вставка в kupiflakon")
  except Exception as e:
      print(f"Ошибка ввода данных: {e}")
      db_connection.rollback()
  finally:
    if db_connection:
        db_connection.close()

def repeated_insert():
    filename = 'db_info.ini'
    section = 'postgres-sample-db'
    db_info = get_db_info(filename, section)
    try:
        with psycopg2.connect(**db_info) as db_connection:
            with db_connection.cursor() as db_cursor:
                n = int(input("Введите номер заказа: "))
                db_cursor.execute('SELECT * FROM kupiflakon WHERE number = %s;', (n,))
                print(str(db_cursor.fetchall()))
                i = int(input("Введите id: "))
                p = input("Количество мест: ")
                d = datetime.now().strftime('%y-%m-%d')
                print("""
                    Выберете статус:
                        1 - Повтор
                        2 - Ошибка
                        3 - Возврат
                    """)
                ones = ['Повтор', 'Ошибка', 'Возврат']
                j = int(input("Статус: "))
                word = ones[j-1]
                insert_record = 'INSERT INTO repeated (id, repeat, place, date) VALUES (%s, %s, %s, %s)'
                insert_value = (i, word, p, d)
                db_cursor.execute(insert_record, insert_value)
            db_connection.commit()
            print("Успешная вставка вrepeated")
    except Exception as e:
        print(f"Ошибка ввода данных: {e}")
        db_connection.rollback()
    finally:
        if db_connection:
            db_connection.close()

def jambs_insert():
  filename = 'db_info.ini'
  section = 'postgres-sample-db'
  db_info = get_db_info(filename, section)
  try:
      with psycopg2.connect(**db_info) as db_connection:
          with db_connection.cursor() as db_cursor:
              n = int(input("Введите номер заказа: "))
              db_cursor.execute('SELECT * FROM kupiflakon WHERE number = %s;', (n,))
              print(str(db_cursor.fetchall()))
              i = int(input("Введите id: "))
              p = input("Количество мест: ")
              d = datetime.now().strftime('%y-%m-%d')
              print("""
                  Выберете статус:
                      1 - Ошибка
                      2 - Недовложение
                      3 - Лишнее
                  """)
              ones = ['Ошибка', 'Недовложение', 'Лишнее']
              j = int(input("Статус: "))
              word = ones[j-1]
              insert_record = 'INSERT INTO jambs (id, jamb, place, date) VALUES (%s, %s, %s, %s)'
              insert_value = (i, word, p, d)
              db_cursor.execute(insert_record, insert_value)
          db_connection.commit()
          print("Успешная вставка в jambs")
  except Exception as e:
      print(f"Ошибка ввода данных: {e}")
      db_connection.rollback()
  finally:
      if db_connection:
          db_connection.close()


def duplicates_search():
    try:
      conn = connect(param_dict)
      if conn is None:
        return
      column_names = ['Номер заказа', 'Количество']
      df = postgresql_to_dataframe(conn,"SELECT number, COUNT(*) FROM kupiflakon GROUP BY number HAVING COUNT(*) > 1 and number IS NOT NULL", column_names)
      if df is None:
          print("Нет данных")
      elif len(df) > 0:
        print(df.head())
      else:
        print("Нет данных")
    except Exception as e:
      print(f"Произошла ошибка: {e}")
    finally:
      if conn:
        conn.close()
# Main execution
if __name__ == "__main__":
  while True:
      print("""
Выберите действие:
   
    1 - Поиск заказа по номеру
    2 - Показать заказы за сегодня
    3 - Зафиксировать конец обработки заказа
    4 - Зафиксировать начало обработки заказа
    5 - Внести данные о суммах заказов
    6 - Внести данные в kupiflakon
    7 - Вывести данные по заказу и сумме за определенный период
    8 - Обновить данные о месте
    9 - Занести данные в repeated
    10 - Занести данные в jambs
    11 - Поиск дубликатов
    0 - Выход

""")
      choice = input("Ваш выбор: ")
      if choice == "1":
          number_search()
      elif choice == "2":
          orders_today()
      elif choice == "3":
         time_end()
      elif choice == "4":
        time_start()
      elif choice == "5":
        money_records()
      elif choice == "6":
        kupiflakon_insert()
      elif choice == "7":
        info_order()
      elif choice == "8":
        update_kupiflakon()
      elif choice == "9":
        repeated_insert()
      elif choice == "10":
        jambs_insert()
      elif choice == "11":
          duplicates_search()
      elif choice == "0":
          break
      else:
          print("Неверный выбор. Попробуйте снова.")
print("Соединение с PostgreSQL закрыто")
