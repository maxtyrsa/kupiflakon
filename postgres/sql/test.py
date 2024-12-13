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

    column_names = ["number", "count"]
# Execute the "SELECT *" query
    df = postgresql_to_dataframe(conn, "SELECT  number, COUNT(*) FROM kupiflakon GROUP BY number HAVING COUNT(*) > 1 and number != 0", column_names)
    if df.len(df) >= 1:
        print(df.head(30))
    elif df.len(df) < 1:
        print("No data")
except:
    if len(df) >= 1:
        print(df[['number', 'count']])
    else:
        print("No data")
