import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")
    
    # connect to MySQL
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

mycursor = conn.cursor()

# show databases
mycursor.execute("SHOW DATABASES")

# mycursor.execute("CREATE DATABASE IF NOT EXISTS imdb_analysis")

for x in mycursor:
    print(x)

conn.close()