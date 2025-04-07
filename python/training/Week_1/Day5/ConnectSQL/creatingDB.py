import mysql.connector

myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="garyfelix",
)

mycursor = myDB.cursor()
# mycursor.execute("CREATE DATABASE rev_db")
# show databases
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)

myDB.close()