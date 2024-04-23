#para instalar el conector de python utilizamos la siguiente libreria: 
# pip install mysql-connector-python

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="pos"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM productos")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
