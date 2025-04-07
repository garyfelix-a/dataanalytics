import mysql.connector

myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="garyfelix",
    database="rev_db"
)

mycursor = myDB.cursor()
mycursor.execute("CREATE TABLE students (name VARCHAR(255), address VARCHAR(255))")

myDB.close()