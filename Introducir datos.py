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

#Seleccionar tabla e Introducir datos
tabla = input('¿Dónde desea introducir los datos? : ').lower()

os.system('cls')

if tabla == 'doctores':
    cédula_dato = input('Introduzca el número de cédula: ')
    nombre_dato = input('Introduzca el nombre: ').capitalize()
    apellido_dato = input('Introduzca el apellido: ').capitalize()
    teléfono_dato = input('Introduzca el teléfono: ')
    correo_electrónico_dato = input('Introduzca el correo electrónico: ')
    dirección_dato = input('Introduzca el dirección: ').capitalize()
    especialidad_dato = input('1.Pediatra - 2.Otorrinolaringólogo/a - 3.Oftalmólogo/a - 4.Psiquiatra - 5.Psicólogo/a\n6.Médico/a General - 7.Cardiólogo/a - 8.Ginecólogo/a - 9.Ortopeda - 10.Dermatologo/a\nEliga el rol: ')
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


elif tabla == 'empleados':
    cédula_dato = input('Introduzca el número de cédula: ')
    nombre_dato = input('Introduzca el nombre: ').capitalize()
    apellido_dato = input('Introduzca el apellido: ').capitalize()
    teléfono_dato = input('Introduzca el teléfono: ')
    correo_electrónico_dato = input('Introduzca el correo electrónico: ')
    dirección_dato = input('Introduzca el dirección: ').capitalize()
    rol_dato = input('1.Enfermero - 2.Limpieza - 3.Mantenimiento\nIntroduzca el rol: ')
    if rol_dato == '1':
        rango_dato = input('1.Encargado General - 2.Encargado - 3.Auxiliar\nEliga el rango: ')
        if rango_dato == '1':
            sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')
            if sexo == '1':
                rango_dato = 'Encargado General'
            if sexo == '2':
                rango_dato = 'Encargada General'
        elif rango_dato == '2':
            sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')
            if sexo == '1':
                rango_dato = 'Encargado'
            if sexo == '2':
                rango_dato = 'Encargada'
        elif rango_dato == '3':
            rango_dato = 'Auxiliar'
    elif rol_dato == '2':
        rango_dato = input('1.Encargado General - 2.Auxiliar\nEliga el rango: ')
        if rango_dato == '1':
            sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')
            if sexo == '1':
                rango_dato = 'Encargado General'
            if sexo == '2':
                rango_dato = 'Encargada General'
        elif rango_dato == '2':
            rango_dato = 'Auxiliar'
    elif rol_dato == '3':
        rango_dato = input('1.Encargado General - 2.Auxiliar\nEliga el rol: ')
        if rango_dato == '1':
            sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')
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

elif tabla == 'insumos':
    código_dato = input('Introudzca el código: ').upper()
    nombre_dato = input('Introduzca el nombre: ').capitalize()
    estado_dato = input('1.En Existencia - 2.Fuera de Existencia\nIntroduzca el estado: ')
    if estado_dato == 1:
        estado_dato = 'En Existencia'
        cantidad_dato = input('Introduzca la cantidad: ')
    elif estado_dato == 2:
        estado_dato = 'Fuera de Existencia'
        cantidad_dato = '0'
    tipo_dato = input('1.Utensilios - 2.Gastables - 3.Medicamentos\nIntroduzca el tipo: ')
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
        forma_dato = input('1.Oral - 2.Pastilla - 3.Inyectado\nIntroduzca la forma del medicamento: ').lower()
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

elif tabla == 'pacientes':
    cédula_dato = input('Introduzca el número de cédula: ')
    nombre_dato = input('Introduzca el nombre: ').capitalize()
    apellido_dato = input('Introduzca el apellido: ').capitalize()
    teléfono_dato = input('Introduzca el teléfono: ')
    correo_electrónico_dato = input('Introduzca el correo electrónico: ')
    dirección_dato = input('Introduzca el dirección: ').capitalize()
    datos = f'{cédula_dato}',f'{nombre_dato}',f'{apellido_dato}',f'{teléfono_dato}',f'{correo_electrónico_dato}',f'{dirección_dato}'
    sql_insertar_pacientes = f"insert into {tabla} (Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección) VALUES (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql_insertar_pacientes,datos)
    mydb.commit()

for x in mycursor:
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
