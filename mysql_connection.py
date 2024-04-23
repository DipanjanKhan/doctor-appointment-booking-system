import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv(".env")

def mysql_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("host"),
            user=os.getenv("db_username"),
            password=os.getenv("db_password"),
            database=os.getenv("database_name")
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print("Error connecting to MySQL database:", e)

if __name__ == "__main__":
    mysql_connection()