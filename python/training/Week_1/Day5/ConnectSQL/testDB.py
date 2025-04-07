import mysql.connector

myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="garyfelix",
)

print(myDB)