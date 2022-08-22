import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Esconder2!",
  database="Hospital"
)

mycursor = mydb.cursor()

sql = "INSERT INTO estudiante (nombre, telefono) VALUES (%s, %s)"
val = ("John", "Highway 21")

mycursor.execute(sql, val)

mydb.commit()

mycursor.execute("select * from estudiante")

for x in mycursor:
    print(x)

print(mycursor.rowcount, "record inserted.")