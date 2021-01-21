import psycopg2
from psycopg2 import pool

query = "INSERT INTO main_table (request, response, request_type) VALUES(%s,%s,%s)"

def database(record_to_insert):
    try:
        postgreSQL_pool = psycopg2.pool.SimpleConnectionPool(1, 20, user="postgres",
                                                  password="annawintour",
                                                  host="172.20.10.14",
                                                  port = "5432",
                                                  database = "dbMeraki")
        if(postgreSQL_pool):
            print("Connection pool created successfully")

        ps_connection = postgreSQL_pool.getconn()

        if (ps_connection):

            print("successfully recived connection from connection pool ")
            ps_cursor = ps_connection.cursor()
            ps_cursor.execute(query, record_to_insert)
            ps_connection.commit()
            count = ps_cursor.rowcount
            print(count, "Record inserted successfully into main_table")

            # Use this method to release the connection object and send back to connection pool
            postgreSQL_pool.putconn(ps_connection)
            print("Put away a PostgreSQL connection")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        #closing database connection.
        # use closeall method to close all the active connection if you want to turn of the application
        if (postgreSQL_pool):
            postgreSQL_pool.closeall
        print("PostgreSQL connection pool is closed")