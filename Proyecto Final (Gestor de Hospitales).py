# Paquetes
import mysql.connector
import os, sys
import time

# Entrada a la base de datos
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Esconder2!",
    database ="hospital"
    )

# Menu
def mostrar_menu(opciones):
    os.system('cls')
    print('Manejador de Hospital')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

# Opciones del "Menu"
def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
        time.sleep(2)
        os.system('cls')
        mostrar_menu(opciones)
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()

# Menu de Opciones
def menu_principal():
    opciones = {
        '1': ('Introducir datos', accion1),
        '2': ('Eliminar datos', accion2),
        '3': ('Ver datos', accion3),
        '4': ('Cambiar datos', accion4),
        '5': ('Salir', salir)
    }
    generar_menu(opciones, '5')


#Introducir datos a una tabla
def accion1():
    os.system('cls')
    mycursor = mydb.cursor()
    mycursor.execute('show tables')
    for x in mycursor:
        print(x)
    tabla = input('¿Dónde desea introducir los datos? : ').lower() # Tabla en la que se quiere introducir los nuevo datos
    os.system('cls')
    if tabla == 'doctores': # Introducir datos de un nuevo "Doctor"
        cédula_dato = input('Introduzca el número de cédula: ')[:11]
        nombre_dato = input('Introduzca el nombre: ').capitalize()[:100]
        apellido_dato = input('Introduzca el apellido: ').capitalize()[:100]
        teléfono_dato = input('Introduzca el teléfono: ')[:10]
        correo_electrónico_dato = input('Introduzca el correo electrónico: ')[:70]
        dirección_dato = input('Introduzca el dirección: ').capitalize()
        especialidad_dato = input('1.Pediatra - 2.Otorrinolaringólogo/a - 3.Oftalmólogo/a - 4.Psiquiatra - 5.Psicólogo/a\n6.Médico/a General - 7.Cardiólogo/a - 8.Ginecólogo/a - 9.Ortopeda - 10.Dermatologo/a\nEliga el rol: ')[:1]
        if especialidad_dato == '1':
            especialidad_dato = 'Pediatra'
        elif especialidad_dato == '2':
            sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')
            if sexo == '1':
                especialidad_dato = 'Otorrinolaringólogo'
            if sexo == '2':
                especialidad_dato = 'Otorrinolaringóloga'
        elif especialidad_dato == '3':
            sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')
            if sexo == '1':
                especialidad_dato = 'Oftalmólogo'
            if sexo == '2':
                especialidad_dato = 'Oftalmóloga'
        elif especialidad_dato == '4':
            especialidad_dato = 'Psiquiatra'
        elif especialidad_dato == '5':
            sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')
            if sexo == '1':
                especialidad_dato = 'Oftalmólogo'
            if sexo == '2':
                especialidad_dato = 'Oftalmóloga'
        elif especialidad_dato == '6':
            sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')
            if sexo == '1':
                especialidad_dato = 'Médico General'
            if sexo == '2':
                especialidad_dato = 'Médica General'
        elif especialidad_dato == '7':
            sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')
            if sexo == '1':
                especialidad_dato = 'Cardiólogo'
            if sexo == '2':
                especialidad_dato = 'Cardióloga'
        elif especialidad_dato == '8':
            sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')
            if sexo == '1':
                especialidad_dato = 'Ginecólogo'
            if sexo == '2':
                especialidad_dato = 'Ginecóloga'
        elif especialidad_dato == '9':
            especialidad_dato = 'Ortopeda'
        elif especialidad_dato == '10':
            sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')
            if sexo == '1':
                especialidad_dato = 'Dermatologo'
            if sexo == '2':
                especialidad_dato = 'Dermatologa'
        datos = f'{cédula_dato}',f'{nombre_dato}',f'{apellido_dato}',f'{teléfono_dato}',f'{correo_electrónico_dato}',f'{dirección_dato}',f'{especialidad_dato}'
        sql_insertar_doctores = f"insert into {tabla} (Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Especialidad) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(sql_insertar_doctores,datos)
        mydb.commit()
    elif tabla == 'empleados':# Introducir datos de un nuevo "Empleado"
        cédula_dato = input('Introduzca el número de cédula: ')[:11]
        nombre_dato = input('Introduzca el nombre: ').capitalize()[:100]
        apellido_dato = input('Introduzca el apellido: ').capitalize()[:100]
        teléfono_dato = input('Introduzca el teléfono: ')[:10]
        correo_electrónico_dato = input('Introduzca el correo electrónico: ')[:70]
        dirección_dato = input('Introduzca el dirección: ').capitalize()
        rol_dato = input('1.Enfermero - 2.Limpieza - 3.Mantenimiento\nIntroduzca el rol: ')[:1]
        if rol_dato == '1':
            rango_dato = input('1.Encargado General - 2.Encargado - 3.Auxiliar\nEliga el rango: ')[:1]
            if rango_dato == '1':
                sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')[:1]
                if sexo == '1':
                    rango_dato = 'Encargado General'
                if sexo == '2':
                    rango_dato = 'Encargada General'
            elif rango_dato == '2':
                sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')[:1]
                if sexo == '1':
                    rango_dato = 'Encargado'
                if sexo == '2':
                    rango_dato = 'Encargada'
            elif rango_dato == '3':
                rango_dato = 'Auxiliar'
        elif rol_dato == '2':
            rango_dato = input('1.Encargado General - 2.Auxiliar\nEliga el rango: ')[:1]
            if rango_dato == '1':
                sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')[:1]
                if sexo == '1':
                    rango_dato = 'Encargado General'
                if sexo == '2':
                    rango_dato = 'Encargada General'
            elif rango_dato == '2':
                rango_dato = 'Auxiliar'
        elif rol_dato == '3':
            rango_dato = input('1.Encargado General - 2.Auxiliar\nEliga el rol: ')[:1]
            if rango_dato == '1':
                sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')[:1]
                if sexo == '1':
                    rango_dato = 'Encargado General'
                if sexo == '2':
                    rango_dato = 'Encargada General'
            elif rango_dato == '2':
                rango_dato = 'Auxiliar'
        datos = f'{cédula_dato}',f'{nombre_dato}',f'{apellido_dato}',f'{teléfono_dato}',f'{correo_electrónico_dato}',f'{dirección_dato}',f'{rango_dato}',f'{rol_dato}'
        sql_insertar_empleados = f"insert into {tabla} (Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Rol, Rango) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(sql_insertar_empleados,datos)
        mydb.commit()
    elif tabla == 'insumos':# Introducir datos de un nuevo "Insumo"
        código_dato = input('Introudzca el código: ').upper()[:10]
        nombre_dato = input('Introduzca el nombre: ').capitalize()[:100]
        estado_dato = input('1.En Existencia - 2.Fuera de Existencia\nIntroduzca el estado: ')[:1]
        if estado_dato == 1:
            estado_dato = 'En Existencia'
            cantidad_dato = input('Introduzca la cantidad: ')[:10000]
        elif estado_dato == 2:
            estado_dato = 'Fuera de Existencia'
            cantidad_dato = '0'
        tipo_dato = input('1.Utensilios - 2.Gastables - 3.Medicamentos\nIntroduzca el tipo: ')[:1]
        if tipo_dato == '1':
            tipo_dato = 'Utensilio'
            datos = f'{código_dato}',f'{nombre_dato}',f'{estado_dato}',f'{cantidad_dato}',f'{tipo_dato}'
            sql_insertar_insumo = f"insert into {tabla} (Código, Nombre, Estado, Cantidad, Tipo) VALUES (%s,%s,%s,%s,%s)"
        if tipo_dato == '2':
            tipo_dato = 'Gastable'
            datos = f'{código_dato}',f'{nombre_dato}',f'{estado_dato}',f'{cantidad_dato}',f'{tipo_dato}'
            sql_insertar_insumo = f"insert into {tabla} (Código, Nombre, Estado, Cantidad, Tipo) VALUES (%s,%s,%s,%s,%s)"
        elif tipo_dato == "3":
            tipo_dato = 'Medicamento'
            forma_dato = input('1.Oral - 2.Pastilla - 3.Inyectado\nIntroduzca la forma del medicamento: ').lower()[:1]
            if forma_dato == '1':
                forma_dato = 'Oral'
            elif forma_dato == '2':
                forma_dato = 'Pastilla'
            elif forma_dato == '3':
                forma_dato = 'Inyectado'
            datos = f'{código_dato}',f'{nombre_dato}',f'{estado_dato}',f'{cantidad_dato}',f'{tipo_dato}',f'{forma_dato}'
            sql_insertar_insumo = f"insert into {tabla} (Código, Nombre, Estado, Cantidad, Tipo, Forma) VALUES (%s,%s,%s,%s,%s,%s)"
        mycursor.execute(sql_insertar_insumo,datos)
        mydb.commit()
    elif tabla == 'pacientes': # Introducir datos de un nuevo "Paciente"
        cédula_dato = input('Introduzca el número de cédula: ')[:11]
        nombre_dato = input('Introduzca el nombre: ').capitalize()[:100]
        apellido_dato = input('Introduzca el apellido: ').capitalize()[:100]
        teléfono_dato = input('Introduzca el teléfono: ')[:10]
        correo_electrónico_dato = input('Introduzca el correo electrónico: ')[:70]
        dirección_dato = input('Introduzca el dirección: ').capitalize()
        datos = f'{cédula_dato}',f'{nombre_dato}',f'{apellido_dato}',f'{teléfono_dato}',f'{correo_electrónico_dato}',f'{dirección_dato}'
        sql_insertar_pacientes = f"insert into {tabla} (Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección) VALUES (%s,%s,%s,%s,%s,%s)"
        mycursor.execute(sql_insertar_pacientes,datos)
        mydb.commit()
        for x in mycursor:
            print (x)
    while True: # Vuelva al Menu Principal
        salir = input('\n\nPresiona "Enter" para volver al Menú Principal:')
        if salir == '':
            os.system('cls')
            print("Volviendo al Menú Principal", end=""); time.sleep(0.3)
            print(".", end=""); time.sleep(0.3)
            print(".", end=""); time.sleep(0.3)
            print(".")
            break
        elif salir != '':
            print('Favor Presionar "Enter" para volver al Menú Principal')
            time.sleep(2)
            os.system('cls')



#Eliminar datos de una tabla
def accion2():
    os.system('cls')
    mycursor = mydb.cursor()
    mycursor.execute('show tables')
    for x in mycursor:
        print(x)
    salida_eliminar = '0'
    tabla = input('¿Dónde desea buscar los datos?: ').lower() # Tabla en la que se quiere introducir los nuevo datos
    os.system('cls')
    if tabla == 'doctores': # Eliminar datos de un "Doctor"
        mycursor.execute('select * from '+tabla)
        myresult = mycursor.fetchall()
        for x in myresult:
            print (x)
        cédula_dato = input('\nIntroduzca el número de cédula: ')[:11] # Cedula del dato que se quiere eliminar
        sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Especialidad from {tabla} where Cédula = '{cédula_dato}'"
        mycursor.execute(sql_selección)
        myresult = mycursor.fetchall()
        while salida_eliminar == '0':
            print("Buscando", end=""); time.sleep(0.66)
            print(".", end=""); time.sleep(0.66)
            print(".", end=""); time.sleep(0.66)
            print(".")
            os.system('cls')
            for x in myresult:
                print (x)
            validacion = input('Ese es el dato que desea eliminar?(Y/N): ').upper()[:1] # Confirmacion del dato buscado
            if validacion == 'Y':
                mycursor.execute('set sql_safe_updates = 0')
                sql_eliminar = f"delete from {tabla} where Cédula = '{cédula_dato}'"
                mycursor.execute(sql_eliminar)
                mycursor.execute('set sql_safe_updates = 1')
                mydb.commit()
                print(mycursor.rowcount, "datos(s) borrados")
                while True:
                    confirmacion = input('\nDesea ver la tabla?(Y/N): ').upper()[:1] # Confirmacion de visualizacion de la tabla
                    if confirmacion == 'Y':
                        mycursor.execute("select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Especialidad from " +tabla)
                        myresult = mycursor.fetchall()
                        for x in myresult:
                            print (x)
                        salida_eliminar = '1'
                        break
                    elif confirmacion == 'N':
                        salida_eliminar = '1'
                        break
                    else:
                        print('Favor introducir una de las opciones dadas')
                        os.system('cls')
            elif validacion == 'N':
                os.system('cls')
                print('Por favor introduzca el dato que desea')
                time.sleep(2)
                os.system('cls')
                mycursor.execute('select * from '+tabla)
                myresult = mycursor.fetchall()
                for x in myresult:
                    print (x)
                cédula_dato = input('Introduzca el número de cédula: ')[:11] # Cedula del dato que se quiere eliminar
                sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Especialidad from {tabla} where Cédula = '{cédula_dato}'"
                mycursor.execute(sql_selección)
                myresult = mycursor.fetchall()
            else:
                print('Esta opcion no es válida')
                time.sleep(2)
                os.system('cls')
    elif tabla == 'empleados':# Eliminar datos de un "Empleado"
        mycursor.execute('select * from '+tabla)
        myresult = mycursor.fetchall()
        for x in myresult:
            print (x)
        cédula_dato = input('Introduzca el número de cédula: ')[:11] # Cedula del dato que se quiere eliminar
        sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Rol, Rango from {tabla} where Cédula = '{cédula_dato}'"
        mycursor.execute(sql_selección)
        myresult = mycursor.fetchall()
        while salida_eliminar == '0':
            print("Buscando", end=""); time.sleep(0.66)
            print(".", end=""); time.sleep(0.66)
            print(".", end=""); time.sleep(0.66)
            print(".")
            for x in myresult:
                print (x)
            validacion = input('Ese es el dato que desea eliminar?(Y/N): ').upper()[:1]# Confirmacion del dato buscado
            if validacion == 'Y':
                mycursor.execute('set sql_safe_updates = 0')
                sql_eliminar = f"delete from {tabla} where Cédula = '{cédula_dato}'"
                mycursor.execute(sql_eliminar)
                mycursor.execute('set sql_safe_updates = 1')
                mydb.commit()
                print(mycursor.rowcount, "datos(s) borrados")
                while True:
                    confirmacion = input('\nDesea ver la tabla?(Y/N): ').upper()[:1]# Confirmacion de visualizacion de la tabla
                    if confirmacion == 'Y':
                        mycursor.execute("select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Rol, Rango from " +tabla)
                        myresult = mycursor.fetchall()
                        for x in myresult:
                            print (x)
                        salida_eliminar = '1'
                        break
                    elif confirmacion == 'N':
                        salida_eliminar = '1'
                        break
                    else:
                        print('Favor introducir una de las opciones dadas')
                        os.system('cls')
            elif validacion == 'N':
                os.system('cls')
                print('Por favor introduzca el dato que desea')
                time.sleep(2)
                os.system('cls')
                mycursor.execute('select * from '+tabla)
                myresult = mycursor.fetchall()
                for x in myresult:
                    print (x)
                cédula_dato = input('Introduzca el número de cédula: ')[:11]# Cedula del dato que se quiere eliminar
                sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Rol, Rango from {tabla} where Cédula = '{cédula_dato}'"
                mycursor.execute(sql_selección)
                myresult = mycursor.fetchall()
            else:
                print('Esta opcion no es válida')
                time.sleep(2)
                os.system('cls')
    elif tabla == 'insumos':# Eliminar datos de un "Insumo"
        mycursor.execute('select * from '+tabla)
        myresult = mycursor.fetchall()
        for x in myresult:
            print (x)
        código_dato = input('Introduzca el número del código: ')[:10]# Codigo del dato que se quiere eliminar
        sql_selección = f"select Código, Nombre, Estado, Cantidad, Tipo, Forma from {tabla} where Código = '{código_dato}'"
        mycursor.execute(sql_selección)
        myresult = mycursor.fetchall()
        while salida_eliminar == '0':
            print("Buscando", end=""); time.sleep(0.66)
            print(".", end=""); time.sleep(0.66)
            print(".", end=""); time.sleep(0.66)
            print(".")
            for x in myresult:
                print (x)
            validacion = input('Ese es el dato que desea eliminar?(Y/N): ').upper()[:1]# Confirmacion del dato buscado
            if validacion == 'Y':
                mycursor.execute('set sql_safe_updates = 0')
                sql_eliminar = f"delete from {tabla} where Código = '{código_dato}'"
                mycursor.execute(sql_eliminar)
                mycursor.execute('set sql_safe_updates = 1')
                mydb.commit()
                print(mycursor.rowcount, "datos(s) borrados")
                while True:
                    confirmacion = input('\nDesea ver la tabla?(Y/N): ').upper()[:1]# Confirmacion de visualizacion de la tabla
                    if confirmacion == 'Y':
                        mycursor.execute("select Código, Nombre, Estado, Cantidad, Tipo, Forma from " +tabla)
                        myresult = mycursor.fetchall()
                        for x in myresult:
                            print (x)
                        salida_eliminar = '1'
                        break
                    elif confirmacion == 'N':
                        salida_eliminar = '1'
                        break
                    else:
                        print('Favor introducir una de las opciones dadas')
                        os.system('cls')
            elif validacion == 'N':
                os.system('cls')
                print('Por favor introduzca el dato que desea')
                time.sleep(2)
                os.system('cls')
                mycursor.execute('select * from '+tabla)
                myresult = mycursor.fetchall()
                for x in myresult:
                    print (x)
                cédula_dato = input('Introduzca el número de codigo: ')[:10]# Codigo del dato que se quiere eliminar
                sql_selección = f"select Código, Nombre, Estado, Cantidad, Tipo, Forma from {tabla} where Código = '{código_dato}'"
                mycursor.execute(sql_selección)
                myresult = mycursor.fetchall()
            else:
                print('Esta opcion no es válida')
                time.sleep(2)
                os.system('cls')
    elif tabla == 'pacientes': # Eliminar datos de un "Paciente"
        mycursor.execute('select * from '+tabla)
        myresult = mycursor.fetchall()
        for x in myresult:
            print (x)
        cédula_dato = input('\nIntroduzca el número de cédula: ')[:11]# Cedula del dato que se quiere eliminar
        sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección from {tabla} where Cédula = '{cédula_dato}'"
        mycursor.execute(sql_selección)
        myresult = mycursor.fetchall()
        while salida_eliminar == '0':
            print("Buscando", end=""); time.sleep(0.66)
            print(".", end=""); time.sleep(0.66)
            print(".", end=""); time.sleep(0.66)
            print(".")
            os.system('cls')
            for x in myresult:
                print (x)
            validacion = input('Ese es el dato que desea eliminar?(Y/N): ').upper()[:1]# Confirmacion del dato buscado
            if validacion == 'Y':
                mycursor.execute('set sql_safe_updates = 0')
                sql_eliminar = f"delete from {tabla} where Cédula = '{cédula_dato}'"
                mycursor.execute(sql_eliminar)
                mycursor.execute('set sql_safe_updates = 1')
                mydb.commit()
                print(mycursor.rowcount, "datos(s) borrados")
                while True:
                    confirmacion = input('\nDesea ver la tabla?(Y/N): ').upper()[:1]# Confirmacion de visualizacion de la tabla
                    if confirmacion == 'Y':
                        mycursor.execute("select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección from " +tabla)
                        myresult = mycursor.fetchall()
                        for x in myresult:
                            print (x)
                        salida_eliminar = '1'
                        break
                    elif confirmacion == 'N':
                        salida_eliminar = '1'
                        break
                    else:
                        print('Favor introducir una de las opciones dadas')
                        os.system('cls')
            elif validacion == 'N':
                os.system('cls')
                print('Por favor introduzca el dato que desea')
                time.sleep(2)
                os.system('cls')
                mycursor.execute('select * from '+tabla)
                myresult = mycursor.fetchall()
                for x in myresult:
                    print (x)
                cédula_dato = input('Introduzca el número de cédula: ')[:11]# Cedula del dato que se quiere eliminar
                sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección from {tabla} where Cédula = '{cédula_dato}'"
                mycursor.execute(sql_selección)
                myresult = mycursor.fetchall()
            else:
                print('Esta opcion no es válida')
                time.sleep(2)
                os.system('cls')
    while True:# Vuelva al Menu Principal
        salir = input('\n\nPresiona "Enter" para volver al Menú Principal:')
        if salir == '':
            os.system('cls')
            print("Volviendo al Menú Principal", end=""); time.sleep(0.3)
            print(".", end=""); time.sleep(0.3)
            print(".", end=""); time.sleep(0.3)
            print(".")
            break
        elif salir != '':
            print('Favor Presionar "Enter" para volver al Menú Principal')
            time.sleep(2)
            os.system('cls')


#Ver datos de una tabla
def accion3():
    os.system('cls')
    mycursor = mydb.cursor()
    mycursor.execute('show tables')
    for x in mycursor:
        print(x)
    tabla = input('¿Qué datos deseas ver?: ').lower()# Tabla en la que se quiere ver los nuevo datos
    os.system('cls')
    if tabla == 'doctores':# Ver datos de "Doctores"
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
    elif tabla == 'empleados':# Ver datos de "Empleados"
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
    elif tabla == 'insumos':# Ver datos de "Insumos"
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
    elif tabla == 'pacientes':# Ver datos de "Pacientes"
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
    while True:# Vuelva al Menu Principal
        salir = input('\n\nPresiona "Enter" para volver al Menú Principal:')
        if salir == '':
            os.system('cls')
            print("Volviendo al Menú Principal", end=""); time.sleep(0.3)
            print(".", end=""); time.sleep(0.3)
            print(".", end=""); time.sleep(0.3)
            print(".")
            break
        elif salir != '':
            print('Favor Presionar "Enter" para volver al Menú Principal')
            time.sleep(2)
            os.system('cls')



#Cambiar datos de una tabla
def accion4():
    os.system('cls')
    mycursor = mydb.cursor()
    mycursor.execute('show tables')
    for x in mycursor:
        print(x)
    tabla = input('¿Dónde desea buscar los datos?: ').lower()# Tabla en la que se quiere ver los nuevo datos
    validacion_cambio = 'Y'
    escape = '0'
    os.system('cls')
    if tabla == 'doctores':# Cambiar datos de un "Doctor"
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
        while escape == '0':
            nueva_cédula_dato = input('\nIntroduzca el número de cédula a buscar: ')[:11]# Cedula del dato a buscar
            sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Especialidad from {tabla} where Cédula = '{nueva_cédula_dato}'"
            mycursor.execute(sql_selección)
            myresult = mycursor.fetchall()
            print("Buscando", end=""); time.sleep(0.66)
            print(".", end=""); time.sleep(0.66)
            print(".", end=""); time.sleep(0.66)
            print(".")
            os.system('cls')
            for x in myresult:
                print (x)
            validacion = input('Ese es el dato que desea cambiar?(Y/N): ').upper()[:1]# Confirmacion del dato buscado
            while validacion_cambio == 'Y':
                if validacion == 'Y':
                    sql_cambio = input('\n1.Cédula - 2.Nombre - 3.Apellido - 4.Teléfono - 5.Correo Electrónico - 6.Dirección - 7.Especialidad\nQué desea cambiar?: ')[:1]
                    os.system('cls')
                    if sql_cambio == '1':# Cambio de cedula
                        for x in myresult:
                            print (x)
                        cédula_dato = input('Introduzca el número de cédula actual: ')[:11]
                        nueva_cédula_dato = input('Introduzca el nuevo número de cédula: ')[:11]
                        sql_ejecutor = f"update {tabla} set Cédula = {nueva_cédula_dato} where Cédula = {cédula_dato}"
                        mycursor.execute(sql_ejecutor)
                        mydb.commit()
                        sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Especialidad from {tabla} where Cédula = '{nueva_cédula_dato}'"
                        mycursor.execute(sql_selección)
                        myresult = mycursor.fetchall()
                    if sql_cambio == '2':# Cambio de nombre
                        for x in myresult:
                            print (x)
                        nombre_dato = input('Introduzca el nombre actual: ').capitalize()[:100]
                        nuevo_nombre_dato = input('Introduzca el nuevo nombre: ').capitalize()[:100]
                        sql_ejecutor = f"update {tabla} set Nombre = '{nuevo_nombre_dato}' where Nombre = '{nombre_dato}'"
                        mycursor.execute(sql_ejecutor)
                        mydb.commit()
                        sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Especialidad from {tabla} where Cédula = '{nueva_cédula_dato}'"
                        mycursor.execute(sql_selección)
                        myresult = mycursor.fetchall()
                    if sql_cambio == '3':# Cambio de apellido
                        for x in myresult:
                            print (x)
                        apellido_dato = input('Introduzca el apellido actual: ').capitalize()[:100]
                        nuevo_apellido_dato = input('Introduzca el nuevo apellido: ').capitalize()[:100]
                        sql_ejecutor = f"update {tabla} set Apellido = '{nuevo_apellido_dato}' where Apellido = '{apellido_dato}'"
                        mycursor.execute(sql_ejecutor)
                        mydb.commit()
                        sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Especialidad from {tabla} where Cédula = '{nueva_cédula_dato}'"
                        mycursor.execute(sql_selección)
                        myresult = mycursor.fetchall()
                    if sql_cambio == '4':# Cambio de telefono
                        for x in myresult:
                            print (x)
                        teléfono_dato = input('Introduzca el teléfono actual: ')[:10]
                        nuevo_telefono_dato = input('Introduzca el nuevo teléfono: ')[:10]
                        sql_ejecutor = f"update {tabla} set Teléfono = '{nuevo_telefono_dato}' where Teléfono = '{teléfono_dato}'"
                        mycursor.execute(sql_ejecutor)
                        mydb.commit()
                        sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Especialidad from {tabla} where Cédula = '{nueva_cédula_dato}'"
                        mycursor.execute(sql_selección)
                        myresult = mycursor.fetchall()
                    if sql_cambio == '5':# Cambio de correo electronico
                        for x in myresult:
                            print (x)
                        correo_electrónico_dato = input('Introduzca el Correo Electrónico actual: ')[:70]
                        nuevo_correo_electrónico_dato = input('Introduzca el nuevo Correo Electrónico: ')[:70]
                        sql_ejecutor = f"update {tabla} set Correo_Electrónico = '{nuevo_correo_electrónico_dato}' where Correo_Electrónico = '{correo_electrónico_dato}'"
                        mycursor.execute(sql_ejecutor)
                        mydb.commit()
                        sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Especialidad from {tabla} where Cédula = '{nueva_cédula_dato}'"
                        mycursor.execute(sql_selección)
                        myresult = mycursor.fetchall()
                    if sql_cambio == '6':# Cambio de direccion
                        for x in myresult:
                            print (x)
                        dirección_dato = input('Introduzca la Dirección actual: ').capitalize()
                        nueva_dirección_dato = input('Introduzca la nuevo Dirección: ').capitalize()
                        sql_ejecutor = f"update {tabla} set Dirección = '{nueva_dirección_dato}' where Dirección = '{dirección_dato}'"
                        mycursor.execute(sql_ejecutor)
                        mydb.commit()
                        sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Especialidad from {tabla} where Cédula = '{nueva_cédula_dato}'"
                        mycursor.execute(sql_selección)
                        myresult = mycursor.fetchall()
                    if sql_cambio == '7':# Cambio de especialidad
                        for x in myresult:
                            print (x)
                        especialidad_dato = input('1.Pediatra - 2.Otorrinolaringólogo/a - 3.Oftalmólogo/a - 4.Psiquiatra - 5.Psicólogo/a\n6.Médico/a General - 7.Cardiólogo/a - 8.Ginecólogo/a - 9.Ortopeda - 10.Dermatologo/a\nIntroduzca la Especialidad actual: ')[:1]
                        if especialidad_dato == '1':
                            especialidad_dato = 'Pediatra'
                        elif especialidad_dato == '2':
                            sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')[:1]
                            if sexo == '1':
                                especialidad_dato = 'Otorrinolaringólogo'
                            if sexo == '2':
                                especialidad_dato = 'Otorrinolaringóloga'
                        elif especialidad_dato == '3':
                            sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')[:1]
                            if sexo == '1':
                                especialidad_dato = 'Oftalmólogo'
                            if sexo == '2':
                                especialidad_dato = 'Oftalmóloga'
                        elif especialidad_dato == '4':
                            especialidad_dato = 'Psiquiatra'
                        elif especialidad_dato == '5':
                            sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')[:1]
                            if sexo == '1':
                                especialidad_dato = 'Oftalmólogo'
                            if sexo == '2':
                                especialidad_dato = 'Oftalmóloga'
                        elif especialidad_dato == '6':
                            sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')[:1]
                            if sexo == '1':
                                especialidad_dato = 'Médico General'
                            if sexo == '2':
                                especialidad_dato = 'Médica General'
                        elif especialidad_dato == '7':
                            sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')[:1]
                            if sexo == '1':
                                especialidad_dato = 'Cardiólogo'
                            if sexo == '2':
                                especialidad_dato = 'Cardióloga'
                        elif especialidad_dato == '8':
                            sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')[:1]
                            if sexo == '1':
                                especialidad_dato = 'Ginecólogo'
                            if sexo == '2':
                                especialidad_dato = 'Ginecóloga'
                        elif especialidad_dato == '9':
                            especialidad_dato = 'Ortopeda'
                        elif especialidad_dato == '10':
                            sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')[:1]
                            if sexo == '1':
                                especialidad_dato = 'Dermatologo'
                            if sexo == '2':
                                especialidad_dato = 'Dermatologa'
                        nueva_especialidad_dato = input('\n1.Pediatra - 2.Otorrinolaringólogo/a - 3.Oftalmólogo/a - 4.Psiquiatra - 5.Psicólogo/a\n6.Médico/a General - 7.Cardiólogo/a - 8.Ginecólogo/a - 9.Ortopeda - 10.Dermatologo/a\nIntroduzca la nueva Especialidad: ')[:1]
                        if nueva_especialidad_dato == '1':
                            nueva_especialidad_dato = 'Pediatra'
                        elif nueva_especialidad_dato == '2':
                            sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')[:1]
                            if sexo == '1':
                                nueva_especialidad_dato = 'Otorrinolaringólogo'
                            if sexo == '2':
                                nueva_especialidad_dato = 'Otorrinolaringóloga'
                        elif nueva_especialidad_dato == '3':
                            sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')[:1]
                            if sexo == '1':
                                nueva_especialidad_dato = 'Oftalmólogo'
                            if sexo == '2':
                                nueva_especialidad_dato = 'Oftalmóloga'
                        elif nueva_especialidad_dato == '4':
                            nueva_especialidad_dato = 'Psiquiatra'
                        elif nueva_especialidad_dato == '5':
                            sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')[:1]
                            if sexo == '1':
                                nueva_especialidad_dato = 'Oftalmólogo'
                            if sexo == '2':
                                nueva_especialidad_dato = 'Oftalmóloga'
                        elif nueva_especialidad_dato == '6':
                            sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')[:1]
                            if sexo == '1':
                                nueva_especialidad_dato = 'Médico General'
                            if sexo == '2':
                                nueva_especialidad_dato = 'Médica General'
                        elif nueva_especialidad_dato == '7':
                            sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')[:1]
                            if sexo == '1':
                                nueva_especialidad_dato = 'Cardiólogo'
                            if sexo == '2':
                                nueva_especialidad_dato = 'Cardióloga'
                        elif nueva_especialidad_dato == '8':
                            sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')[:1]
                            if sexo == '1':
                                nueva_especialidad_dato = 'Ginecólogo'
                            if sexo == '2':
                                nueva_especialidad_dato = 'Ginecóloga'
                        elif nueva_especialidad_dato == '9':
                            nueva_especialidad_dato = 'Ortopeda'
                        elif nueva_especialidad_dato == '10':
                            sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')[:1]
                            if sexo == '1':
                                nueva_especialidad_dato = 'Dermatologo'
                            if sexo == '2':
                                nueva_especialidad_dato = 'Dermatologa'
                        sql_ejecutor = f"update {tabla} set Especialidad = '{nueva_especialidad_dato}' where Especialidad = '{especialidad_dato}'"
                        mycursor.execute(sql_ejecutor)
                        mydb.commit()
                        sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Especialidad from {tabla} where Cédula = '{nueva_cédula_dato}'"
                        mycursor.execute(sql_selección)
                        myresult = mycursor.fetchall()
                    while True:
                        os.system('cls')
                        for x in myresult:
                            print (x)
                        validacion_cambio = input('\nDesea continuar haciendo cambios?(Y/N): ').upper()[:1]# Confirmacion de continuacion de cambios
                        if validacion_cambio == 'Y':
                            break
                        elif validacion_cambio == 'N':
                            escape = '1'
                            break
                        else:
                            print('Esta opcion no es válida')
                            time.sleep(2)
                            os.system('cls')
                elif validacion == 'N':
                    validacion_cambio = 'N'
                    os.system('cls')
    elif tabla == 'empleados':# Cambiar datos de un "Empleado"
        sql_buscador = f'select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Rol, Rango from {tabla} order by Nombre'
        mycursor.execute(sql_buscador)
        myresult = mycursor.fetchall()
        print("Cargando", end=""); time.sleep(0.5)
        print(".", end=""); time.sleep(0.5)
        print(".", end=""); time.sleep(0.5)
        print(".")
        os.system('cls')
        for x in myresult:
            print (x)
        while escape == '0':
            nueva_cédula_dato = input('\nIntroduzca el número de cédula a buscar: ')[:11]# Cedula del dato a buscar
            sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Rol, Rango from {tabla} where Cédula = '{nueva_cédula_dato}'"
            mycursor.execute(sql_selección)
            myresult = mycursor.fetchall()
            print("Buscando", end=""); time.sleep(0.66)
            print(".", end=""); time.sleep(0.66)
            print(".", end=""); time.sleep(0.66)
            print(".")
            os.system('cls')
            for x in myresult:
                print (x)
            validacion = input('Ese es el dato que desea cambiar?(Y/N): ').upper()[:1]# Confirmacion del dato buscado
            while validacion_cambio == 'Y':
                if validacion == 'Y':
                    sql_cambio = input('\n1.Cédula - 2.Nombre - 3.Apellido - 4.Teléfono - 5.Correo Electrónico - 6.Dirección - 7.Rol - 8.Rango\nQué desea cambiar?: ')[:1]
                    os.system('cls')
                    if sql_cambio == '1':# Cambio de cedula
                        for x in myresult:
                            print (x)
                        cédula_dato = input('Introduzca el número de cédula actual: ')[:11]
                        nueva_cédula_dato = input('Introduzca el nuevo número de cédula: ')[:11]
                        sql_ejecutor = f"update {tabla} set Cédula = {nueva_cédula_dato} where Cédula = {cédula_dato}"
                        mycursor.execute(sql_ejecutor)
                        mydb.commit()
                        sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Rol, Rango from {tabla} where Cédula = '{nueva_cédula_dato}'"
                        mycursor.execute(sql_selección)
                        myresult = mycursor.fetchall()
                    if sql_cambio == '2':# Cambio de nombre
                        for x in myresult:
                            print (x)
                        nombre_dato = input('Introduzca el nombre actual: ').capitalize()[:100]
                        nuevo_nombre_dato = input('Introduzca el nuevo nombre: ').capitalize()[:100]
                        sql_ejecutor = f"update {tabla} set Nombre = '{nuevo_nombre_dato}' where Nombre = '{nombre_dato}'"
                        mycursor.execute(sql_ejecutor)
                        mydb.commit()
                        sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Rol, Rango from {tabla} where Cédula = '{nueva_cédula_dato}'"
                        mycursor.execute(sql_selección)
                        myresult = mycursor.fetchall()
                    if sql_cambio == '3':# Cambio de apellido
                        for x in myresult:
                            print (x)
                        apellido_dato = input('Introduzca el apellido actual: ').capitalize()[:100]
                        nuevo_apellido_dato = input('Introduzca el nuevo apellido: ').capitalize()[:100]
                        sql_ejecutor = f"update {tabla} set Apellido = '{nuevo_apellido_dato}' where Apellido = '{apellido_dato}'"
                        mycursor.execute(sql_ejecutor)
                        mydb.commit()
                        sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Rol, Rango from {tabla} where Cédula = '{nueva_cédula_dato}'"
                        mycursor.execute(sql_selección)
                        myresult = mycursor.fetchall()
                    if sql_cambio == '4':# Cambio de telefono
                        for x in myresult:
                            print (x)
                        teléfono_dato = input('Introduzca el teléfono actual: ')[:10]
                        nuevo_telefono_dato = input('Introduzca el nuevo teléfono: ')[:100]
                        sql_ejecutor = f"update {tabla} set Teléfono = '{nuevo_telefono_dato}' where Teléfono = '{teléfono_dato}'"
                        mycursor.execute(sql_ejecutor)
                        mydb.commit()
                        sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Rol, Rango from {tabla} where Cédula = '{nueva_cédula_dato}'"
                        mycursor.execute(sql_selección)
                        myresult = mycursor.fetchall()
                    if sql_cambio == '5':# Cambio de correo electronico
                        for x in myresult:
                            print (x)
                        correo_electrónico_dato = input('Introduzca el Correo Electrónico actual: ')[:70]
                        nuevo_correo_electrónico_dato = input('Introduzca el nuevo Correo Electrónico: ')[:70]
                        sql_ejecutor = f"update {tabla} set Correo_Electrónico = '{nuevo_correo_electrónico_dato}' where Correo_Electrónico = '{correo_electrónico_dato}'"
                        mycursor.execute(sql_ejecutor)
                        mydb.commit()
                        sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Rol, Rango from {tabla} where Cédula = '{nueva_cédula_dato}'"
                        mycursor.execute(sql_selección)
                        myresult = mycursor.fetchall()
                    if sql_cambio == '6':# Cambio de direccion
                        for x in myresult:
                            print (x)
                        dirección_dato = input('Introduzca la Dirección actual: ').capitalize()
                        nueva_dirección_dato = input('Introduzca la nuevo Dirección: ').capitalize()
                        sql_ejecutor = f"update {tabla} set Dirección = '{nueva_dirección_dato}' where Dirección = '{dirección_dato}'"
                        mycursor.execute(sql_ejecutor)
                        mydb.commit()
                        sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Rol, Rango from {tabla} where Cédula = '{nueva_cédula_dato}'"
                        mycursor.execute(sql_selección)
                        myresult = mycursor.fetchall()
                    if sql_cambio == '7':# Cambio de rol
                        for x in myresult:
                            print (x)
                        rol_dato = input('1.Enfermero - 2.Limpieza - 3.Mantenimiento\nIntroduzca el rol actual: ')[:1]
                        if rol_dato == '1':
                            rol_dato == 'Enfermero'
                        elif rol_dato == '2':
                            rol_dato == 'Limpieza'
                        elif rol_dato == '3':
                            rol_dato == 'Mantenimiento'
                        nuevo_rol_dato = input('\n1.Enfermero - 2.Limpieza - 3.Mantenimiento\nIntroduzca el nuevo rol: ')[:1]
                        if nuevo_rol_dato == '1':
                            nuevo_rol_dato == 'Enfermero'
                        elif nuevo_rol_dato == '2':
                            nuevo_rol_dato == 'Limpieza'
                        elif nuevo_rol_dato == '3':
                            nuevo_rol_dato == 'Mantenimiento'
                        sql_ejecutor = f"update {tabla} set Rol = '{nuevo_rol_dato}' where Rol = '{rol_dato}'"
                        mycursor.execute(sql_ejecutor)
                        mydb.commit()
                        sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Rol, Rango from {tabla} where Dirección = '{nuevo_rol_dato}'"
                        mycursor.execute(sql_selección)
                        myresult = mycursor.fetchall()
                    if sql_cambio == '8':# Cambio de rango
                        for x in myresult:
                            print (x)
                        rol_dato = input('1.Enfermero - 2.Limpieza - 3.Mantenimiento\nIntroduzca el rol actual: ')[:1]
                        if rol_dato == '1':
                            rango_dato = input('\n1.Encargado General - 2.Encargado - 3.Auxiliar\nEliga el rango actual: ')[:1]
                            if rango_dato == '1':
                                sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')[:1]
                                if sexo == '1':
                                    rango_dato = 'Encargado General'
                                if sexo == '2':
                                    rango_dato = 'Encargada General'
                            elif rango_dato == '2':
                                sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')[:1]
                                if sexo == '1':
                                    rango_dato = 'Encargado'
                                if sexo == '2':
                                    rango_dato = 'Encargada'
                            elif rango_dato == '3':
                                rango_dato = 'Auxiliar'
                        elif rol_dato == '2':
                            rango_dato = input('\n1.Encargado - 2.Auxiliar\nEliga el rango actual: ')[:1]
                            if rango_dato == '1':
                                sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')[:1]
                                if sexo == '1':
                                    rango_dato = 'Encargado General'
                                if sexo == '2':
                                    rango_dato = 'Encargada General'
                            elif rango_dato == '2':
                                rango_dato = 'Auxiliar'
                        elif rol_dato == '3':
                            rango_dato = input('\n1.Encargado - 2.Auxiliar\nEliga el rango actual: ')[:1]
                            if rango_dato == '1':
                                sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')[:1]
                                if sexo == '1':
                                    rango_dato = 'Encargado General'
                                if sexo == '2':
                                    rango_dato = 'Encargada General'
                            elif rango_dato == '2':
                                rango_dato = 'Auxiliar'
                        if rol_dato == '1':
                            nuevo_rango_dato = input('\n1.Encargado General - 2.Encargado - 3.Auxiliar\nEliga el nuevo rango: ')[:1]
                            if nuevo_rango_dato == '1':
                                sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')[:1]
                                if sexo == '1':
                                    nuevo_rango_dato = 'Encargado General'
                                if sexo == '2':
                                    nuevo_rango_dato = 'Encargada General'
                            elif nuevo_rango_dato == '2':
                                sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')[:1]
                                if sexo == '1':
                                    nuevo_rango_dato = 'Encargado'
                                if sexo == '2':
                                    nuevo_rango_dato = 'Encargada'
                            elif nuevo_rango_dato == '3':
                                nuevo_rol_dato = 'Auxiliar'
                        elif rol_dato == '2':
                            nuevo_rango_dato = input('\n1.Encargado - 2.Auxiliar\nEliga el nuevo rango: ')[:1]
                            if nuevo_rango_dato == '1':
                                sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')
                                if sexo == '1':
                                    nuevo_rango_dato = 'Encargado General'
                                if sexo == '2':
                                    nuevo_rango_dato = 'Encargada General'
                            elif nuevo_rango_dato == '2':
                                nuevo_rango_dato = 'Auxiliar'
                        elif rol_dato == '3':
                            nuevo_rango_dato = input('\n1.Encargado - 2.Auxiliar\nEliga el rango: ')[:1]
                            if nuevo_rango_dato == '1':
                                sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')[:1]
                                if sexo == '1':
                                    nuevo_rango_dato = 'Encargado General'
                                if sexo == '2':
                                    nuevo_rango_dato = 'Encargada General'
                            elif nuevo_rango_dato == '2':
                                nuevo_rango_dato = 'Auxiliar'
                        sql_ejecutor = f"update {tabla} set Rango = '{nuevo_rango_dato}' where Rango = '{rango_dato}'" 
                        mycursor.execute(sql_ejecutor)
                        mydb.commit()
                        sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Rol, Rango from {tabla} where Dirección = '{nuevo_rango_dato}'"
                        mycursor.execute(sql_selección)
                        myresult = mycursor.fetchall()
                    while True:
                        os.system('cls')
                        for x in myresult:
                            print (x)
                        validacion_cambio = input('\nDesea continuar haciendo cambios?(Y/N): ').upper()[:1]# Confirmacion de continuacion de cambios
                        if validacion_cambio == 'Y':
                            break
                        elif validacion_cambio == 'N':
                            escape = '1'
                            break
                        else:
                            print('Esta opcion no es válida')
                            time.sleep(2)
                            os.system('cls')
                elif validacion == 'N':
                    validacion_cambio = 'N'
                    os.system('cls')
    elif tabla == 'insumos':# Cambiar datos de un "Insumo"
        sql_buscador = f'select Código, Nombre, Estado, Cantidad, Tipo from {tabla} order by Nombre'
        mycursor.execute(sql_buscador)
        myresult = mycursor.fetchall()
        print("Cargando", end=""); time.sleep(0.5)
        print(".", end=""); time.sleep(0.5)
        print(".", end=""); time.sleep(0.5)
        print(".")
        os.system('cls')
        for x in myresult:
            print (x)
        while escape == '0':
            nuevo_código_dato = input('\nIntroduzca el número de código a buscar: ')[:10]# Codigo del dato a buscar
            sql_selección = f"select Código, Nombre, Estado, Cantidad, Tipo from {tabla} where Código = '{código_dato}'"
            mycursor.execute(sql_selección)
            myresult = mycursor.fetchall()
            print("Buscando", end=""); time.sleep(0.66)
            print(".", end=""); time.sleep(0.66)
            print(".", end=""); time.sleep(0.66)
            print(".")
            os.system('cls')
            for x in myresult:
                print (x)
            validacion = input('Ese es el dato que desea cambiar?(Y/N): ').upper()[:1]# Confirmacion del dato buscado
            validacion_cambio = 'Y'
            while validacion_cambio == 'Y':
                if validacion == 'Y':
                    sql_cambio = input('\n1.Código - 2.Nombre - 3.Estado - 4.Tipo - 5.Forma\nQué desea cambiar?: ')[:1]
                    os.system('cls')
                    if sql_cambio == '1':# Cambio de codigo
                        for x in myresult:
                            print (x)
                        código_dato = input('Introduzca el número de código actual: ').upper()[:10]
                        nuevo_código_dato = input('Introduzca el nuevo número de código: ').upper()[:10]
                        sql_ejecutor = f'update {tabla} set Código = {nuevo_código_dato} where Código = {código_dato}'
                        mycursor.execute(sql_ejecutor)
                        mydb.commit()
                        sql_selección = f"select Código, Nombre, Estado, Cantidad, Tipo from {tabla} where Código = '{nuevo_código_dato}'"
                        mycursor.execute(sql_selección)
                        myresult = mycursor.fetchall()
                    if sql_cambio == '2':# Cambio de nombre
                        for x in myresult:
                            print (x)
                        nombre_dato = input('Introduzca el nombre actual: ').capitalize()[:100]
                        nuevo_nombre_dato = input('Introduzca el nuevo nombre: ').capitalize()[:100]
                        sql_ejecutor = f"update {tabla} set Nombre = '{nuevo_nombre_dato}' where Nombre = '{nombre_dato}'"
                        mycursor.execute(sql_ejecutor)
                        mydb.commit()
                        sql_selección = f"select Código, Nombre, Estado, Cantidad, Tipo from {tabla} where Código = '{nuevo_código_dato}'"
                        mycursor.execute(sql_selección)
                        myresult = mycursor.fetchall()
                    if sql_cambio == '3':# Cambio de estado
                        for x in myresult:
                            print (x)
                        estado_dato = input('1.En Existencia - 2.Fuera de Existencia\nIntroduzca el estado actual: ')[:1]
                        if estado_dato == '1':
                            estado_dato = 'En Existencia'
                        elif estado_dato == '2':
                            estado_dato = 'Fuera de Existencia'
                        nuevo_estado_dato = input('1.En Existencia - 2.Fuera de Existencia\nIntroduzca el nuevo estado: ')[:1]
                        if nuevo_estado_dato == '1':
                            nuevo_estado_dato = 'En Existencia'
                            sql_ejecutor = f"update {tabla} set Cantidad = '1' where Código = '{nuevo_código_dato}'"
                            mycursor.execute(sql_ejecutor)
                            mydb.commit()
                        elif nuevo_estado_dato == '2':
                            nuevo_estado_dato = 'Fuera de Existencia'
                            sql_ejecutor = f"update {tabla} set Cantidad = '0' where Código = '{nuevo_código_dato}'"
                            mycursor.execute(sql_ejecutor)
                            mydb.commit()
                        sql_ejecutor = f"update {tabla} set Estado = '{nuevo_estado_dato}' where Estado = '{estado_dato}'"
                        mycursor.execute(sql_ejecutor)
                        mydb.commit()
                        sql_selección = f"select Código, Nombre, Estado, Cantidad, Tipo from {tabla} where Código = '{nuevo_código_dato}'"
                        mycursor.execute(sql_selección)
                        myresult = mycursor.fetchall()
                    if sql_cambio == '4':# Cambio de cantidad
                        for x in myresult:
                            print (x)
                        cantidad_dato = input('Introduzca la cantidad actual: ')[:10000]
                        nueva_cantidad_dato = input('Introduzca la nueva cantidad: ')[:10000]
                        if nueva_cantidad_dato == '0':
                            sql_ejecutor = f"update {tabla} set Estado = 'Fuera de Existencia' where Código = '{nuevo_código_dato}'"
                            mycursor.execute(sql_ejecutor)
                            mydb.commit()
                        if nueva_cantidad_dato >= '0':
                            sql_ejecutor = f"update {tabla} set Estado = 'En Existencia' where Código = '{nuevo_código_dato}'"
                            mycursor.execute(sql_ejecutor)
                            mydb.commit()
                        sql_ejecutor = f"update {tabla} set Cantidad = '{nueva_cantidad_dato}' where Cantidad = '{cantidad_dato}'"
                        mycursor.execute(sql_ejecutor)
                        mydb.commit()
                        sql_selección = f"select Código, Nombre, Estado, Cantidad, Tipo from {tabla} where Código = '{nuevo_código_dato}'"
                        mycursor.execute(sql_selección)
                        myresult = mycursor.fetchall()
                    if sql_cambio == '5':# Cambio de tipo
                        for x in myresult:
                            print (x)
                        tipo_dato = input('1.Utensilios - 2.Gastables - 3.Medicamentos\nIntroduzca el tipo actual: ')[:1]
                        if tipo_dato == '1':
                            tipo_dato = 'Utensilio'
                        elif tipo_dato == '2':
                            tipo_dato = 'Gastable'
                        elif tipo_dato == "3":
                            tipo_dato = 'Medicamento'
                        nuevo_tipo_dato = input('1.Utensilios - 2.Gastables - 3.Medicamentos\nIntroduzca el nuevo tipo: ')[:1]
                        if nuevo_tipo_dato == '1':
                            nuevo_tipo_dato = 'Utensilio'
                        elif nuevo_tipo_dato == '2':
                            nuevo_tipo_dato = 'Gastable'
                        elif nuevo_tipo_dato == "3":
                            nuevo_tipo_dato = 'Medicamento'
                        sql_ejecutor = f"update {tabla} set Tipo = '{tipo_dato}' where Tipo = '{nuevo_tipo_dato}'"
                        mycursor.execute(sql_ejecutor)
                        mydb.commit()
                        sql_selección = f"select Código, Nombre, Estado, Cantidad, Tipo from {tabla} where Código = '{nuevo_código_dato}'"
                        mycursor.execute(sql_selección)
                        myresult = mycursor.fetchall()
                    if sql_cambio == '6':# Cambio de forma
                        for x in myresult:
                            print (x)
                        forma_dato = input('1.Oral - 2.Pastilla - 3.Inyectado\nIntroduzca la actual forma del medicamento: ')[:1]
                        if forma_dato == '1':
                            forma_dato = 'Oral'
                        elif forma_dato == '2':
                            forma_dato = 'Pastilla'
                        elif forma_dato == '3':
                            forma_dato = 'Inyectado'
                        nueva_forma_dato = input('1.Oral - 2.Pastilla - 3.Inyectado\nIntroduzca la nueva forma del medicamento: ')[:1]
                        if nueva_forma_dato == '1':
                            nueva_forma_dato = 'Oral'
                        elif forma_dato == '2':
                            nueva_forma_dato = 'Pastilla'
                        elif forma_dato == '3':
                            nueva_forma_dato = 'Inyectado'
                        sql_ejecutor = f"update {tabla} set Forma = '{nueva_forma_dato}' where Forma = '{forma_dato}'"
                        mycursor.execute(sql_ejecutor)
                        mydb.commit()
                        sql_selección = f"select Código, Nombre, Estado, Cantidad, Tipo, Forma from {tabla} where Código = '{nuevo_código_dato}'"
                        mycursor.execute(sql_selección)
                        myresult = mycursor.fetchall()
                        while True:
                            os.system('cls')
                            for x in myresult:
                                print (x)
                            validacion_cambio = input('\nDesea continuar haciendo cambios?(Y/N): ').upper()[:1]# Confirmacion de continuacion de cambios
                            if validacion_cambio == 'Y':
                                break
                            elif validacion_cambio == 'N':
                                escape = '1'
                                break
                            else:
                                print('Esta opcion no es válida')
                                time.sleep(2)
                                os.system('cls')
                elif validacion == 'N':
                    validacion_cambio = 'N'
                    os.system('cls')
    elif tabla == 'pacientes':# Cambiar datos de un "Pacientes"
        sql_buscador = f'select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección from {tabla} order by Nombre'
        mycursor.execute(sql_buscador)
        myresult = mycursor.fetchall()
        print("Cargando", end=""); time.sleep(0.5)
        print(".", end=""); time.sleep(0.5)
        print(".", end=""); time.sleep(0.5)
        print(".")
        os.system('cls')
        for x in myresult:
            print (x)
        while escape == '0':
            nueva_cédula_dato = input('\nIntroduzca el número de cédula a buscar: ')[:11]# Cedula del dato a buscar
            sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección from {tabla} where Cédula = '{nueva_cédula_dato}'"
            mycursor.execute(sql_selección)
            myresult = mycursor.fetchall()
            print("Buscando", end=""); time.sleep(0.66)
            print(".", end=""); time.sleep(0.66)
            print(".", end=""); time.sleep(0.66)
            print(".")
            os.system('cls')
            for x in myresult:
                print (x)
            validacion = input('Ese es el dato que desea cambiar?(Y/N): ').upper()[:1]# Confirmacion del dato buscado
            while validacion_cambio == 'Y':
                if validacion == 'Y':
                    sql_cambio = input('\n1.Cédula - 2.Nombre - 3.Apellido - 4.Teléfono - 5.Correo Electrónico - 6.Dirección\nQué desea cambiar?: ')[:11]
                    os.system('cls')
                    if sql_cambio == '1':# Cambio de cedula
                        for x in myresult:
                            print (x)
                        cédula_dato = input('Introduzca el número de cédula actual: ')[:11]
                        nueva_cédula_dato = input('Introduzca el nuevo número de cédula: ')[:11]
                        sql_ejecutor = f"update {tabla} set Cédula = {nueva_cédula_dato} where Cédula = {cédula_dato}"
                        mycursor.execute(sql_ejecutor)
                        mydb.commit()
                        sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección from {tabla} where Cédula = '{nueva_cédula_dato}'"
                        mycursor.execute(sql_selección)
                        myresult = mycursor.fetchall()
                    if sql_cambio == '2':# Cambio de nombre
                        for x in myresult:
                            print (x)
                        nombre_dato = input('Introduzca el nombre actual: ').capitalize()[:100]
                        nuevo_nombre_dato = input('Introduzca el nuevo nombre: ').capitalize()[:100]
                        sql_ejecutor = f"update {tabla} set Nombre = '{nuevo_nombre_dato}' where Nombre = '{nombre_dato}'"
                        mycursor.execute(sql_ejecutor)
                        mydb.commit()
                        sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección from {tabla} where Cédula = '{nueva_cédula_dato}'"
                        mycursor.execute(sql_selección)
                        myresult = mycursor.fetchall()
                    if sql_cambio == '3':# Cambio de apellido
                        for x in myresult:
                            print (x)
                        apellido_dato = input('Introduzca el apellido actual: ').capitalize()[:100]
                        nuevo_apellido_dato = input('Introduzca el nuevo apellido: ').capitalize()[:100]
                        sql_ejecutor = f"update {tabla} set Apellido = '{nuevo_apellido_dato}' where Apellido = '{apellido_dato}'"
                        mycursor.execute(sql_ejecutor)
                        mydb.commit()
                        sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección from {tabla} where Cédula = '{nueva_cédula_dato}'"
                        mycursor.execute(sql_selección)
                        myresult = mycursor.fetchall()
                    if sql_cambio == '4':# Cambio de telefono
                        for x in myresult:
                            print (x)
                        teléfono_dato = input('Introduzca el teléfono actual: ')[:10]
                        nuevo_telefono_dato = input('Introduzca el nuevo teléfono: ')[:10]
                        sql_ejecutor = f"update {tabla} set Teléfono = '{nuevo_telefono_dato}' where Teléfono = '{teléfono_dato}'"
                        mycursor.execute(sql_ejecutor)
                        mydb.commit()
                        sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección from {tabla} where Cédula = '{nueva_cédula_dato}'"
                        mycursor.execute(sql_selección)
                        myresult = mycursor.fetchall()
                    if sql_cambio == '5':# Cambio de correo electronico
                        for x in myresult:
                            print (x)
                        correo_electrónico_dato = input('Introduzca el Correo Electrónico actual: ')[:70]
                        nuevo_correo_electrónico_dato = input('Introduzca el nuevo Correo Electrónico: ')[:70]
                        sql_ejecutor = f"update {tabla} set Correo_Electrónico = '{nuevo_correo_electrónico_dato}' where Correo_Electrónico = '{correo_electrónico_dato}'"
                        mycursor.execute(sql_ejecutor)
                        mydb.commit()
                        sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección from {tabla} where Cédula = '{nueva_cédula_dato}'"
                        mycursor.execute(sql_selección)
                        myresult = mycursor.fetchall()
                    if sql_cambio == '6':# Cambio de direccion
                        for x in myresult:
                            print (x)
                        dirección_dato = input('Introduzca la Dirección actual: ').capitalize()
                        nueva_dirección_dato = input('Introduzca la nuevo Dirección: ').capitalize()
                        sql_ejecutor = f"update {tabla} set Dirección = '{nueva_dirección_dato}' where Dirección = '{dirección_dato}'"
                        mycursor.execute(sql_ejecutor)
                        mydb.commit()
                        sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección from {tabla} where Cédula = '{nueva_cédula_dato}'"
                        mycursor.execute(sql_selección)
                        myresult = mycursor.fetchall()
                    while True:
                        os.system('cls')
                        for x in myresult:
                            print (x)
                        validacion_cambio = input('\nDesea continuar haciendo cambios?(Y/N): ').upper()[:1]# Confirmacion de continuacion de cambios
                        if validacion_cambio == 'Y':
                            break
                        elif validacion_cambio == 'N':
                            escape = '1'
                            break
                        else:
                            print('Esta opcion no es válida')
                            time.sleep(2)
                            os.system('cls')
                elif validacion == 'N':
                    validacion_cambio = 'N'
                    os.system('cls')
    while validacion == 'N':# Vuelva al Menu Principal
        salir = input('\n\nPresiona "Enter" para para volver al Menú Principal:')
        if salir == '':
                os.system('cls')
                print("Volviendo al Menú Principal", end=""); time.sleep(0.3)
                print(".", end=""); time.sleep(0.3)
                print(".", end=""); time.sleep(0.3)
                print(".")
                break
        elif salir != '':
                print('Favor Presionar "Enter" para para volver al Menú Principal')
                time.sleep(2)
                os.system('cls')



#Terminar el programa
def salir():
    os.system('cls')
    print("Saliendo", end=""); time.sleep(0.3)
    print(".", end=""); time.sleep(0.3)
    print(".", end=""); time.sleep(0.3)
    print(".")



if __name__ == '__main__':
    menu_principal()