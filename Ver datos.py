import mysql.connector
import os
import time

os.system('cls')

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Esconder2!",
    database ="hospital"
    )

mycursor = mydb.cursor()

mycursor.execute('show tables')

for x in mycursor:
    print(x)

#Seleccionar eliminar datos de una tabla
tabla = input('¿Qué datos deseas ver?: ').lower()

os.system('cls')

if tabla == 'doctores':
    sql_buscador = f'select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Especialidad from {tabla} order by Nombre'
    mycursor.execute(sql_buscador)
    myresult = mycursor.fetchall()
    print("Cargando", end=""); time.sleep(0.5)
    print(".", end=""); time.sleep(0.5)
    print(".", end=""); time.sleep(0.5)
    print(".")
    os.system('cls')
    for x in myresult:
        print (x)

elif tabla == 'empleados':
    sql_buscador = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Rol, Rango from {tabla} order by Nombre"
    mycursor.execute(sql_buscador)
    myresult = mycursor.fetchall()
    print("Cargando", end=""); time.sleep(0.5)
    print(".", end=""); time.sleep(0.5)
    print(".", end=""); time.sleep(0.5)
    print(".")
    os.system('cls')
    for x in myresult:
        print (x)

elif tabla == 'insumos':
    sql_buscador = f"select Código, Nombre, Estado, Cantidad, Tipo, Forma from {tabla} order by Nombre"
    mycursor.execute(sql_buscador)
    myresult = mycursor.fetchall()
    print("Cargando", end=""); time.sleep(0.5)
    print(".", end=""); time.sleep(0.5)
    print(".", end=""); time.sleep(0.5)
    print(".")
    os.system('cls')
    for x in myresult:
        print (x)


elif tabla == 'pacientes':
    sql_buscador = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección from {tabla} order by Nombre"
    mycursor.execute(sql_buscador)
    myresult = mycursor.fetchall()
    print("Cargando", end=""); time.sleep(0.5)
    print(".", end=""); time.sleep(0.5)
    print(".", end=""); time.sleep(0.5)
    print(".")
    os.system('cls')
    for x in myresult:
        print (x)

while True:
    salir = input('\n\nPresiona "Enter" para salir:')
    if salir == '':
        os.system('cls')
        print("Saliendo", end=""); time.sleep(0.3)
        print(".", end=""); time.sleep(0.3)
        print(".", end=""); time.sleep(0.3)
        print(".")
        break
    elif salir != '':
        print('Favor Presionar "Enter" para salir')
        time.sleep(2)
        os.system('cls')