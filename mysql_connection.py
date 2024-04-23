import mysql.connector
import os
from dotenv import load_dotenv
from mysql.connector import errorcode

load_dotenv(".env")

def mysql_connection():
    try:
        connection = mysql.connector.connect(
            user=os.getenv('db_username'), 
            password=os.getenv('db_password'),                          
            host='127.0.0.1',
            database=os.getenv('database_name')
            )
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

    return connection

