import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database="mydatabase1"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE person (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

