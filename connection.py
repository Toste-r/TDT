import psycopg2


def connection ():
    con = psycopg2.connect(
  database="postgres", 
  user="postgres", 
  password="0192", 
  host="127.0.0.1", 
  port="5432"
)

    #print("Database opened successfully")
    return con