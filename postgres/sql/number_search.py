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
try:
        conn = connect(param_dic)

        column_names = ["id", "date", "number", "place", "t_c", "branch"]
# Execute the "SELECT *" query
        n = int(input("Введите номер заказа: "))
        df = postgresql_to_dataframe(conn, "select * from kupiflakon", column_names)
        order = df.query('number == {}'.format(n))
        order.set_index("id", inplace=True)
        if len(order) >= 1:
            print(order)
        elif len(order) == 0:
            print("No data")
except:
#    if len(df) >= 1:
#        print(df.query('number == {}'.format(n)))
#    elif len(df) < 1:
        print("no")
