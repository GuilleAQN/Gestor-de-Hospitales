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

validacion_cambio = 'Y'

escape = '0'

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
    while escape == '0':
        nueva_cédula_dato = input('\nIntroduzca el número de cédula a buscar: ')
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
        validacion = input('Ese es el dato que desea cambiar?(Y/N): ').upper()
        while validacion_cambio == 'Y':
            if validacion == 'Y':
                sql_cambio = input('\n1.Cédula - 2.Nombre - 3.Apellido - 4.Teléfono - 5.Correo Electrónico - 6.Dirección - 7.Especialidad\nQué desea cambiar?: ')
                os.system('cls')
                if sql_cambio == '1':
                    for x in myresult:
                        print (x)
                    cédula_dato = input('Introduzca el número de cédula actual: ')
                    nueva_cédula_dato = input('Introduzca el nuevo número de cédula: ')
                    sql_ejecutor = f"update {tabla} set Cédula = {nueva_cédula_dato} where Cédula = {cédula_dato}"
                    mycursor.execute(sql_ejecutor)
                    mydb.commit()
                    sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Especialidad from {tabla} where Cédula = '{nueva_cédula_dato}'"
                    mycursor.execute(sql_selección)
                    myresult = mycursor.fetchall()
                if sql_cambio == '2':
                    for x in myresult:
                        print (x)
                    nombre_dato = input('Introduzca el nombre actual: ').capitalize()
                    nuevo_nombre_dato = input('Introduzca el nuevo nombre: ').capitalize()
                    sql_ejecutor = f"update {tabla} set Nombre = '{nuevo_nombre_dato}' where Nombre = '{nombre_dato}'"
                    mycursor.execute(sql_ejecutor)
                    mydb.commit()
                    sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Especialidad from {tabla} where Cédula = '{nueva_cédula_dato}'"
                    mycursor.execute(sql_selección)
                    myresult = mycursor.fetchall()
                if sql_cambio == '3':
                    for x in myresult:
                        print (x)
                    apellido_dato = input('Introduzca el apellido actual: ').capitalize()
                    nuevo_apellido_dato = input('Introduzca el nuevo apellido: ').capitalize()
                    sql_ejecutor = f"update {tabla} set Apellido = '{nuevo_apellido_dato}' where Apellido = '{apellido_dato}'"
                    mycursor.execute(sql_ejecutor)
                    mydb.commit()
                    sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Especialidad from {tabla} where Cédula = '{nueva_cédula_dato}'"
                    mycursor.execute(sql_selección)
                    myresult = mycursor.fetchall()
                if sql_cambio == '4':
                    for x in myresult:
                        print (x)
                    teléfono_dato = input('Introduzca el teléfono actual: ')
                    nuevo_telefono_dato = input('Introduzca el nuevo teléfono: ')
                    sql_ejecutor = f"update {tabla} set Teléfono = '{nuevo_telefono_dato}' where Teléfono = '{teléfono_dato}'"
                    mycursor.execute(sql_ejecutor)
                    mydb.commit()
                    sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Especialidad from {tabla} where Cédula = '{nueva_cédula_dato}'"
                    mycursor.execute(sql_selección)
                    myresult = mycursor.fetchall()
                if sql_cambio == '5':
                    for x in myresult:
                        print (x)
                    correo_electrónico_dato = input('Introduzca el Correo Electrónico actual: ')
                    nuevo_correo_electrónico_dato = input('Introduzca el nuevo Correo Electrónico: ')
                    sql_ejecutor = f"update {tabla} set Correo_Electrónico = '{nuevo_correo_electrónico_dato}' where Correo_Electrónico = '{correo_electrónico_dato}'"
                    mycursor.execute(sql_ejecutor)
                    mydb.commit()
                    sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Especialidad from {tabla} where Cédula = '{nueva_cédula_dato}'"
                    mycursor.execute(sql_selección)
                    myresult = mycursor.fetchall()
                if sql_cambio == '6':
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
                if sql_cambio == '7':
                    for x in myresult:
                        print (x)
                    especialidad_dato = input('1.Pediatra - 2.Otorrinolaringólogo/a - 3.Oftalmólogo/a - 4.Psiquiatra - 5.Psicólogo/a\n6.Médico/a General - 7.Cardiólogo/a - 8.Ginecólogo/a - 9.Ortopeda - 10.Dermatologo/a\nIntroduzca la Especialidad actual: ')
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
                    nueva_especialidad_dato = input('1.Pediatra - 2.Otorrinolaringólogo/a - 3.Oftalmólogo/a - 4.Psiquiatra - 5.Psicólogo/a\n6.Médico/a General - 7.Cardiólogo/a - 8.Ginecólogo/a - 9.Ortopeda - 10.Dermatologo/a\nIntroduzca la nueva Especialidad: ')
                    if nueva_especialidad_dato == '1':
                        nueva_especialidad_dato = 'Pediatra'
                    elif nueva_especialidad_dato == '2':
                        sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')
                        if sexo == '1':
                            nueva_especialidad_dato = 'Otorrinolaringólogo'
                        if sexo == '2':
                            nueva_especialidad_dato = 'Otorrinolaringóloga'
                    elif nueva_especialidad_dato == '3':
                        sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')
                        if sexo == '1':
                            nueva_especialidad_dato = 'Oftalmólogo'
                        if sexo == '2':
                            nueva_especialidad_dato = 'Oftalmóloga'
                    elif nueva_especialidad_dato == '4':
                        nueva_especialidad_dato = 'Psiquiatra'
                    elif nueva_especialidad_dato == '5':
                        sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')
                        if sexo == '1':
                            nueva_especialidad_dato = 'Oftalmólogo'
                        if sexo == '2':
                            nueva_especialidad_dato = 'Oftalmóloga'
                    elif nueva_especialidad_dato == '6':
                        sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')
                        if sexo == '1':
                            nueva_especialidad_dato = 'Médico General'
                        if sexo == '2':
                            nueva_especialidad_dato = 'Médica General'
                    elif nueva_especialidad_dato == '7':
                        sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')
                        if sexo == '1':
                            nueva_especialidad_dato = 'Cardiólogo'
                        if sexo == '2':
                            nueva_especialidad_dato = 'Cardióloga'
                    elif nueva_especialidad_dato == '8':
                        sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')
                        if sexo == '1':
                            nueva_especialidad_dato = 'Ginecólogo'
                        if sexo == '2':
                            nueva_especialidad_dato = 'Ginecóloga'
                    elif nueva_especialidad_dato == '9':
                        nueva_especialidad_dato = 'Ortopeda'
                    elif nueva_especialidad_dato == '10':
                        sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')
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
                    validacion_cambio = input('\nDesea continuar haciendo cambios?(Y/N): ').upper()
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



elif tabla == 'empleados':
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
        nueva_cédula_dato = input('\nIntroduzca el número de cédula a buscar: ')
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
        validacion = input('Ese es el dato que desea cambiar?(Y/N): ').upper()
        while validacion_cambio == 'Y':
            if validacion == 'Y':
                sql_cambio = input('\n1.Cédula - 2.Nombre - 3.Apellido - 4.Teléfono - 5.Correo Electrónico - 6.Dirección - 7.Rol - 8.Rango\nQué desea cambiar?: ')
                os.system('cls')
                if sql_cambio == '1':
                    for x in myresult:
                        print (x)
                    cédula_dato = input('Introduzca el número de cédula actual: ')
                    nueva_cédula_dato = input('Introduzca el nuevo número de cédula: ')
                    sql_ejecutor = f"update {tabla} set Cédula = {nueva_cédula_dato} where Cédula = {cédula_dato}"
                    mycursor.execute(sql_ejecutor)
                    mydb.commit()
                    sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Rol, Rango from {tabla} where Cédula = '{nueva_cédula_dato}'"
                    mycursor.execute(sql_selección)
                    myresult = mycursor.fetchall()
                if sql_cambio == '2':
                    for x in myresult:
                        print (x)
                    nombre_dato = input('Introduzca el nombre actual: ').capitalize()
                    nuevo_nombre_dato = input('Introduzca el nuevo nombre: ').capitalize()
                    sql_ejecutor = f"update {tabla} set Nombre = '{nuevo_nombre_dato}' where Nombre = '{nombre_dato}'"
                    mycursor.execute(sql_ejecutor)
                    mydb.commit()
                    sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Rol, Rango from {tabla} where Cédula = '{nueva_cédula_dato}'"
                    mycursor.execute(sql_selección)
                    myresult = mycursor.fetchall()
                if sql_cambio == '3':
                    for x in myresult:
                        print (x)
                    apellido_dato = input('Introduzca el apellido actual: ').capitalize()
                    nuevo_apellido_dato = input('Introduzca el nuevo apellido: ').capitalize()
                    sql_ejecutor = f"update {tabla} set Apellido = '{nuevo_apellido_dato}' where Apellido = '{apellido_dato}'"
                    mycursor.execute(sql_ejecutor)
                    mydb.commit()
                    sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Rol, Rango from {tabla} where Cédula = '{nueva_cédula_dato}'"
                    mycursor.execute(sql_selección)
                    myresult = mycursor.fetchall()
                if sql_cambio == '4':
                    for x in myresult:
                        print (x)
                    teléfono_dato = input('Introduzca el teléfono actual: ')
                    nuevo_telefono_dato = input('Introduzca el nuevo teléfono: ')
                    sql_ejecutor = f"update {tabla} set Teléfono = '{nuevo_telefono_dato}' where Teléfono = '{teléfono_dato}'"
                    mycursor.execute(sql_ejecutor)
                    mydb.commit()
                    sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Rol, Rango from {tabla} where Cédula = '{nueva_cédula_dato}'"
                    mycursor.execute(sql_selección)
                    myresult = mycursor.fetchall()
                if sql_cambio == '5':
                    for x in myresult:
                        print (x)
                    correo_electrónico_dato = input('Introduzca el Correo Electrónico actual: ')
                    nuevo_correo_electrónico_dato = input('Introduzca el nuevo Correo Electrónico: ')
                    sql_ejecutor = f"update {tabla} set Correo_Electrónico = '{nuevo_correo_electrónico_dato}' where Correo_Electrónico = '{correo_electrónico_dato}'"
                    mycursor.execute(sql_ejecutor)
                    mydb.commit()
                    sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Rol, Rango from {tabla} where Cédula = '{nueva_cédula_dato}'"
                    mycursor.execute(sql_selección)
                    myresult = mycursor.fetchall()
                if sql_cambio == '6':
                    for x in myresult:
                        print (x)
                    dirección_dato = input('Introduzca la Dirección actual: ').capitalize()
                    nueva_dirección_dato = input('Introduzca la nuevo Dirección: ')
                    sql_ejecutor = f"update {tabla} set Dirección = '{nueva_dirección_dato}' where Dirección = '{dirección_dato}'"
                    mycursor.execute(sql_ejecutor)
                    mydb.commit()
                    sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección, Rol, Rango from {tabla} where Cédula = '{nueva_cédula_dato}'"
                    mycursor.execute(sql_selección)
                    myresult = mycursor.fetchall()
                if sql_cambio == '7':
                    for x in myresult:
                        print (x)
                    rol_dato = input('1.Enfermero - 2.Limpieza - 3.Mantenimiento\nIntroduzca el rol actual: ')
                    if rol_dato == '1':
                        rol_dato == 'Enfermero'
                    elif rol_dato == '2':
                        rol_dato == 'Limpieza'
                    elif rol_dato == '3':
                        rol_dato == 'Mantenimiento'
                    nuevo_rol_dato = input('1.Enfermero - 2.Limpieza - 3.Mantenimiento\nIntroduzca el nuevo rol: ')
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
                if sql_cambio == '8':
                    for x in myresult:
                        print (x)
                    rol_dato = input('1.Enfermero - 2.Limpieza - 3.Mantenimiento\nIntroduzca el rol actual: ')
                    if rol_dato == '1':
                        rango_dato = input('1.Encargado General - 2.Encargado - 3.Auxiliar\nEliga el rango actual: ')
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
                        rango_dato = input('1.Encargado - 2.Auxiliar\nEliga el rango actual: ')
                        if rango_dato == '1':
                            sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')
                            if sexo == '1':
                                rango_dato = 'Encargado General'
                            if sexo == '2':
                                rango_dato = 'Encargada General'
                        elif rango_dato == '2':
                            rango_dato = 'Auxiliar'
                    elif rol_dato == '3':
                        rango_dato = input('1.Encargado - 2.Auxiliar\nEliga el rango actual: ')
                        if rango_dato == '1':
                            sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')
                            if sexo == '1':
                                rango_dato = 'Encargado General'
                            if sexo == '2':
                                rango_dato = 'Encargada General'
                        elif rango_dato == '2':
                            rango_dato = 'Auxiliar'
                    if rol_dato == '1':
                        nuevo_rango_dato = input('1.Encargado General - 2.Encargado - 3.Auxiliar\nEliga el nuevo rango: ')
                        if nuevo_rango_dato == '1':
                            sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')
                            if sexo == '1':
                                nuevo_rango_dato = 'Encargado General'
                            if sexo == '2':
                                nuevo_rango_dato = 'Encargada General'
                        elif nuevo_rango_dato == '2':
                            sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')
                            if sexo == '1':
                                nuevo_rango_dato = 'Encargado'
                            if sexo == '2':
                                nuevo_rango_dato = 'Encargada'
                        elif nuevo_rango_dato == '3':
                            nuevo_rol_dato = 'Auxiliar'
                    elif rol_dato == '2':
                        nuevo_rango_dato = input('1.Encargado - 2.Auxiliar\nEliga el nuevo rango: ')
                        if nuevo_rango_dato == '1':
                            sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')
                            if sexo == '1':
                                nuevo_rango_dato = 'Encargado General'
                            if sexo == '2':
                                nuevo_rango_dato = 'Encargada General'
                        elif nuevo_rango_dato == '2':
                            nuevo_rango_dato = 'Auxiliar'
                    elif rol_dato == '3':
                        nuevo_rango_dato = input('1.Encargado - 2.Auxiliar\nEliga el rango: ')
                        if nuevo_rango_dato == '1':
                            sexo = input('1.Hombre - 2.Mujer\nIntroduzca el sexo: ')
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
                    validacion_cambio = input('\nDesea continuar haciendo cambios?(Y/N): ').upper()
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

elif tabla == 'insumos':
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
        nuevo_código_dato = input('\nIntroduzca el número de código a buscar: ')
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
        validacion = input('Ese es el dato que desea cambiar?(Y/N): ').upper()
        validacion_cambio = 'Y'
        while validacion_cambio == 'Y':
            if validacion == 'Y':
                sql_cambio = input('\n1.Código - 2.Nombre - 3.Estado - 4.Tipo - 5.Forma\nQué desea cambiar?: ')
                os.system('cls')
                if sql_cambio == '1':
                    for x in myresult:
                        print (x)
                    código_dato = input('Introduzca el número de código actual: ').upper()
                    nuevo_código_dato = input('Introduzca el nuevo número de código: ').upper()
                    sql_ejecutor = f'update {tabla} set Código = {nuevo_código_dato} where Código = {código_dato}'
                    mycursor.execute(sql_ejecutor)
                    mydb.commit()
                    sql_selección = f"select Código, Nombre, Estado, Cantidad, Tipo from {tabla} where Código = '{nuevo_código_dato}'"
                    mycursor.execute(sql_selección)
                    myresult = mycursor.fetchall()
                if sql_cambio == '2':
                    for x in myresult:
                        print (x)
                    nombre_dato = input('Introduzca el nombre actual: ').capitalize()
                    nuevo_nombre_dato = input('Introduzca el nuevo nombre: ').capitalize()
                    sql_ejecutor = f"update {tabla} set Nombre = '{nuevo_nombre_dato}' where Nombre = '{nombre_dato}'"
                    mycursor.execute(sql_ejecutor)
                    mydb.commit()
                    sql_selección = f"select Código, Nombre, Estado, Cantidad, Tipo from {tabla} where Código = '{nuevo_código_dato}'"
                    mycursor.execute(sql_selección)
                    myresult = mycursor.fetchall()
                if sql_cambio == '3':
                    for x in myresult:
                        print (x)
                    estado_dato = input('1.En Existencia - 2.Fuera de Existencia\nIntroduzca el estado actual: ')
                    if estado_dato == '1':
                        estado_dato = 'En Existencia'
                    elif estado_dato == '2':
                        estado_dato = 'Fuera de Existencia'
                    nuevo_estado_dato = input('1.En Existencia - 2.Fuera de Existencia\nIntroduzca el nuevo estado: ')
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
                if sql_cambio == '4':
                    for x in myresult:
                        print (x)
                    cantidad_dato = input('Introduzca la cantidad actual: ')
                    nueva_cantidad_dato = input('Introduzca la nueva cantidad: ')
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
                if sql_cambio == '5':
                    for x in myresult:
                        print (x)
                    tipo_dato = input('1.Utensilios - 2.Gastables - 3.Medicamentos\nIntroduzca el tipo actual: ')
                    if tipo_dato == '1':
                        tipo_dato = 'Utensilio'
                    elif tipo_dato == '2':
                        tipo_dato = 'Gastable'
                    elif tipo_dato == "3":
                        tipo_dato = 'Medicamento'
                    nuevo_tipo_dato = input('1.Utensilios - 2.Gastables - 3.Medicamentos\nIntroduzca el nuevo tipo: ')
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
                if sql_cambio == '6':
                    for x in myresult:
                        print (x)
                    forma_dato = input('1.Oral - 2.Pastilla - 3.Inyectado\nIntroduzca la actual forma del medicamento: ')
                    if forma_dato == '1':
                        forma_dato = 'Oral'
                    elif forma_dato == '2':
                        forma_dato = 'Pastilla'
                    elif forma_dato == '3':
                        forma_dato = 'Inyectado'
                    nueva_forma_dato = input('1.Oral - 2.Pastilla - 3.Inyectado\nIntroduzca la nueva forma del medicamento: ')
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
                        validacion_cambio = input('\nDesea continuar haciendo cambios?(Y/N): ').upper()
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

elif tabla == 'pacientes':
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
        nueva_cédula_dato = input('\nIntroduzca el número de cédula a buscar: ')
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
        validacion = input('Ese es el dato que desea cambiar?(Y/N): ').upper()
        while validacion_cambio == 'Y':
            if validacion == 'Y':
                sql_cambio = input('\n1.Cédula - 2.Nombre - 3.Apellido - 4.Teléfono - 5.Correo Electrónico - 6.Dirección\nQué desea cambiar?: ')
                os.system('cls')
                if sql_cambio == '1':
                    for x in myresult:
                        print (x)
                    cédula_dato = input('Introduzca el número de cédula actual: ')
                    nueva_cédula_dato = input('Introduzca el nuevo número de cédula: ')
                    sql_ejecutor = f"update {tabla} set Cédula = {nueva_cédula_dato} where Cédula = {cédula_dato}"
                    mycursor.execute(sql_ejecutor)
                    mydb.commit()
                    sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección from {tabla} where Cédula = '{nueva_cédula_dato}'"
                    mycursor.execute(sql_selección)
                    myresult = mycursor.fetchall()
                if sql_cambio == '2':
                    for x in myresult:
                        print (x)
                    nombre_dato = input('Introduzca el nombre actual: ').capitalize()
                    nuevo_nombre_dato = input('Introduzca el nuevo nombre: ').capitalize()
                    sql_ejecutor = f"update {tabla} set Nombre = '{nuevo_nombre_dato}' where Nombre = '{nombre_dato}'"
                    mycursor.execute(sql_ejecutor)
                    mydb.commit()
                    sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección from {tabla} where Cédula = '{nueva_cédula_dato}'"
                    mycursor.execute(sql_selección)
                    myresult = mycursor.fetchall()
                if sql_cambio == '3':
                    for x in myresult:
                        print (x)
                    apellido_dato = input('Introduzca el apellido actual: ').capitalize()
                    nuevo_apellido_dato = input('Introduzca el nuevo apellido: ').capitalize()
                    sql_ejecutor = f"update {tabla} set Apellido = '{nuevo_apellido_dato}' where Apellido = '{apellido_dato}'"
                    mycursor.execute(sql_ejecutor)
                    mydb.commit()
                    sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección from {tabla} where Cédula = '{nueva_cédula_dato}'"
                    mycursor.execute(sql_selección)
                    myresult = mycursor.fetchall()
                if sql_cambio == '4':
                    for x in myresult:
                        print (x)
                    teléfono_dato = input('Introduzca el teléfono actual: ')
                    nuevo_telefono_dato = input('Introduzca el nuevo teléfono: ')
                    sql_ejecutor = f"update {tabla} set Teléfono = '{nuevo_telefono_dato}' where Teléfono = '{teléfono_dato}'"
                    mycursor.execute(sql_ejecutor)
                    mydb.commit()
                    sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección from {tabla} where Cédula = '{nueva_cédula_dato}'"
                    mycursor.execute(sql_selección)
                    myresult = mycursor.fetchall()
                if sql_cambio == '5':
                    for x in myresult:
                        print (x)
                    correo_electrónico_dato = input('Introduzca el Correo Electrónico actual: ')
                    nuevo_correo_electrónico_dato = input('Introduzca el nuevo Correo Electrónico: ')
                    sql_ejecutor = f"update {tabla} set Correo_Electrónico = '{nuevo_correo_electrónico_dato}' where Correo_Electrónico = '{correo_electrónico_dato}'"
                    mycursor.execute(sql_ejecutor)
                    mydb.commit()
                    sql_selección = f"select Cédula, Nombre, Apellido, Teléfono, Correo_Electrónico, Dirección from {tabla} where Cédula = '{nueva_cédula_dato}'"
                    mycursor.execute(sql_selección)
                    myresult = mycursor.fetchall()
                if sql_cambio == '6':
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
                    validacion_cambio = input('\nDesea continuar haciendo cambios?(Y/N): ').upper()
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