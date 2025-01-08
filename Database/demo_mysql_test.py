import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database="mydatabase1"
)
mydb.autocommit = True

mycursor = mydb.cursor()

#mycursor.execute("Create Database mydatabase1")

#mycursor.execute("SHOW DATABASES")

# mycursor.execute("CREATE TABLE person (name VARCHAR(255), address VARCHAR(255))" )
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

mycursor.close()