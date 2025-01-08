import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database="mydatabase1"
)

mycursor = mydb.cursor()

#mycursor.execute("SELECT name,address FROM person")
#mycursor.execute("SELECT * FROM person WHERE address  = 'Park Lane 38'")
#mycursor.execute("SELECT * FROM person WHERE address Like '%way%'")
#mycursor.execute("SELECT * FROM person ORDER BY name DESC")
#myresult = mycursor.fetchall()

mycursor.execute("UPDATE person SET address = 'Canyon 123' WHERE address = 'Valley 345'")

print(mycursor.rowcount, "record(s) affected")
#for x in myresult:
  #print(x)