import psycopg2
import pandas as pd

# Connection parameters, yours will be different
param_dic = {
    "host"      : "pg3.sweb.ru",
    "database"  : "tyrsadocto",
    "user"      : "tyrsadocto",
    "password"  : "T5p2fga5c8y"
}

def connect(params_dic):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1) 
    print("Connection successful")
    return conn
def postgresql_to_dataframe(conn, select_query, column_names):
    """
    Tranform a SELECT query into a pandas dataframe
    """
    cursor = conn.cursor()
    try:
        cursor.execute(select_query)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        cursor.close()
        return 1
    
    # Naturally we get a list of tupples
    tupples = cursor.fetchall()
    cursor.close()
    
    # We just need to turn it into a pandas dataframe
    df = pd.DataFrame(tupples, columns=column_names)
    return df
# Connect to the database
conn = connect(param_dic)

column_names = ["id", "date", "number", "place", "amount", "t_c"]
# Execute the "SELECT *" query
df = postgresql_to_dataframe(conn, "SELECT m.id, date, number, place, m.amount, t_c from kupiflakon as k join money as m on k.id = m.id", column_names)
from datetime import date
import numpy as np
date_start = input('Введите начальную дату в формате YYYY-MM-DD: ').split('-')

year_s, month_s, day_s = [int(item) for item in date_start]

s = date(year_s, month_s, day_s)

date_end = input('Введите конечную дату в формате YYYY-MM-DD: ').split('-')

year_e, month_e, day_e = [int(item) for item in date_end]

e = date(year_e, month_e, day_e)

df = df[df['date'].between(s, e)]
print('Итого:' ,df.amount.sum(), '₽')
print('Количество заказов:', df.place.shape[0], 'шт')
print('Сумма в среднем за один заказ:', round(np.mean(df.amount)), '₽')
