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
tabla = input('¿Dónde desea buscar los datos?: ').lower()

os.system('cls')

if tabla == 'doctores':
    cédula_dato = input('Introduzca el número de cédula: ')
    sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Especialidad from {tabla} where Cédula = '{cédula_dato}'"
    mycursor.execute(sql_selección)
    myresult = mycursor.fetchall()
    while True:
        print("Buscando", end=""); time.sleep(0.66)
        print(".", end=""); time.sleep(0.66)
        print(".", end=""); time.sleep(0.66)
        print(".")
        for x in myresult:
            print (x)
        validacion = input('Ese es el dato que desea eliminar?(Y/N): ').upper()
        if validacion == 'Y':
            mycursor.execute('set sql_safe_updates = 0')
            sql_eliminar = f"delete from {tabla} where Cédula = '{cédula_dato}'"
            mycursor.execute(sql_eliminar)
            mycursor.execute('set sql_safe_updates = 1')
            mydb.commit()
            print(mycursor.rowcount, "datos(s) borrados")
            while True:
                confirmacion = input('Desea ver la tabla?(Y/N): ').upper()
                if confirmacion == 'Y':
                    mycursor.execute("select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Especialidad from " +tabla)
                    myresult = mycursor.fetchall()
                    for x in myresult:
                        print (x)
                    break
                elif confirmacion == 'N':
                    break
                else:
                    print('Favor introducir una de las opciones dadas')
                    os.system('cls')
        elif validacion == 'N':
            os.system('cls')
            print('Por favor introduzca el dato que desea')
            time.sleep(2)
            os.system('cls')
            cédula_dato = input('Introduzca el número de cédula: ')
            sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Especialidad from {tabla} where Cédula = '{cédula_dato}'"
            mycursor.execute(sql_selección)
            myresult = mycursor.fetchall()
        else:
            print('Esta opcion no es válida')
            time.sleep(2)
            os.system('cls')

elif tabla == 'empleados':
    cédula_dato = input('Introduzca el número de cédula: ')
    sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Rol, Rango from {tabla} where Cédula = '{cédula_dato}'"
    mycursor.execute(sql_selección)
    myresult = mycursor.fetchall()
    while True:
        for x in myresult:
            print (x)
        print("Buscando", end=""); time.sleep(0.66)
        print(".", end=""); time.sleep(0.66)
        print(".", end=""); time.sleep(0.66)
        print(".")
        validacion = input('Ese es el dato que desea eliminar?(Y/N): ').upper()
        if validacion == 'Y':
            mycursor.execute('set sql_safe_updates = 0')
            sql_eliminar = f"delete from {tabla} where Cédula = '{cédula_dato}'"
            mycursor.execute(sql_eliminar)
            mycursor.execute('set sql_safe_updates = 1')
            mydb.commit()
            print(mycursor.rowcount, "datos(s) borrados")
            while True:
                confirmacion = input('Desea ver la tabla?(Y/N): ').upper()
                if confirmacion == 'Y':
                    mycursor.execute("select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Rol, Rango from " +tabla)
                    myresult = mycursor.fetchall()
                    for x in myresult:
                        print (x)
                    break
                elif confirmacion == 'N':
                    break
                else:
                    print('Favor introducir una de las opciones dadas')
                    os.system('cls')
        elif validacion == 'N':
            os.system('cls')
            print('Por favor introduzca el dato que desea')
            time.sleep(2)
            os.system('cls')
            cédula_dato = input('Introduzca el número de cédula: ')
            sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Rol, Rango from {tabla} where Cédula = '{cédula_dato}'"
            mycursor.execute(sql_selección)
            myresult = mycursor.fetchall()
        else:
            print('Esta opcion no es válida')
            time.sleep(2)
            os.system('cls')

elif tabla == 'insumos':
    código_dato = input('Introduzca el número del código: ')
    sql_selección = f"select Código, Nombre, Estado, Cantidad, Tipo, Forma from {tabla} where Código = '{código_dato}'"
    mycursor.execute(sql_selección)
    myresult = mycursor.fetchall()
    while True:
        print("Buscando", end=""); time.sleep(0.66)
        print(".", end=""); time.sleep(0.66)
        print(".", end=""); time.sleep(0.66)
        print(".")
        for x in myresult:
            print (x)
        validacion = input('Ese es el dato que desea eliminar?(Y/N): ').upper()
        if validacion == 'Y':
            mycursor.execute('set sql_safe_updates = 0')
            sql_eliminar = f"delete from {tabla} where Código = '{código_dato}'"
            mycursor.execute(sql_eliminar)
            mycursor.execute('set sql_safe_updates = 1')
            mydb.commit()
            print(mycursor.rowcount, "datos(s) borrados")
            while True:
                confirmacion = input('Desea ver la tabla?(Y/N): ').upper()
                if confirmacion == 'Y':
                    mycursor.execute("select Código, Nombre, Estado, Cantidad, Tipo, Forma from " +tabla)
                    myresult = mycursor.fetchall()
                    for x in myresult:
                        print (x)
                    break
                elif confirmacion == 'N':
                    break
                else:
                    print('Favor introducir una de las opciones dadas')
                    os.system('cls')
        elif validacion == 'N':
            os.system('cls')
            print('Por favor introduzca el dato que desea')
            time.sleep(2)
            os.system('cls')
            cédula_dato = input('Introduzca el número de cédula: ')
            sql_selección = f"select Código, Nombre, Estado, Cantidad, Tipo, Forma from {tabla} where Cédula = '{código_dato}'"
            mycursor.execute(sql_selección)
            myresult = mycursor.fetchall()
        else:
            print('Esta opcion no es válida')
            time.sleep(2)
            os.system('cls')

elif tabla == 'pacientes':
    cédula_dato = input('Introduzca el número de cédula: ')
    sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección from {tabla} where Cédula = '{cédula_dato}'"
    mycursor.execute(sql_selección)
    myresult = mycursor.fetchall()
    while True:
        print("Buscando", end=""); time.sleep(0.66)
        print(".", end=""); time.sleep(0.66)
        print(".", end=""); time.sleep(0.66)
        print(".")
        for x in myresult:
            print (x)
        validacion = input('Ese es el dato que desea eliminar?(Y/N): ').upper()
        if validacion == 'Y':
            mycursor.execute('set sql_safe_updates = 0')
            sql_eliminar = f"delete from {tabla} where Cédula = '{cédula_dato}'"
            mycursor.execute(sql_eliminar)
            mycursor.execute('set sql_safe_updates = 1')
            mydb.commit()
            print(mycursor.rowcount, "datos(s) borrados")
            while True:
                confirmacion = input('Desea ver la tabla?(Y/N): ').upper()
                if confirmacion == 'Y':
                    mycursor.execute("select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección from " +tabla)
                    myresult = mycursor.fetchall()
                    for x in myresult:
                        print (x)
                    break
                elif confirmacion == 'N':
                    break
                else:
                    print('Favor introducir una de las opciones dadas')
                    os.system('cls')
        elif validacion == 'N':
            os.system('cls')
            print('Por favor introduzca el dato que desea')
            time.sleep(2)
            os.system('cls')
            cédula_dato = input('Introduzca el número de cédula: ')
            sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección from {tabla} where Cédula = '{cédula_dato}'"
            mycursor.execute(sql_selección)
            myresult = mycursor.fetchall()
        else:
            print('Esta opcion no es válida')
            time.sleep(2)
            os.system('cls')

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