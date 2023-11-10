# Escribir un programa que permita gestionar la base de datos de alumnado de un classroom.
# Los alumnos y alumnas se guardarán en una lista que almacena un diccionario para cada 
# alumno/a en el que la clave de cada alumno/a será su NIF, y el valor será otro diccionario 
# con los datos del alumno/a (nombre, apellidos, teléfono, correo, aprobado), donde aprobado 
# tendrá el valor True si ha aprobado el módulo. El programa debe preguntar al usuario por una 
# opción del siguiente menú: (1) Añadir alumno/a, (2) Eliminar alumno/a, (3) Mostrar alumno/a,
# (4) Listar todo el alumnado, (5) Listar alumnado aprobado, (6) Terminar. En función de la
# opción elegida el programa tendrá que hacer lo siguiente:
# Preguntar los datos del alumno/a, crear un diccionario con los datos y añadirlo a la base de datos.
# Preguntar por el NIF del alumno/a y eliminar sus datos de la base de datos.
# Preguntar por el NIF del alumno/a y mostrar sus datos.
# Mostrar lista de todo el alumnado de la base de datos con su NIF y nombre.
# Mostrar la lista del alumnado aprobado de la base de datos con su NIF y nombre.
# Terminar el programa.
studentsList = [{'22222222A' : {'nombre' : 'ainara', 
                                'apellido' : 'robles',
                                'teléfono' : 661698953,
                                'correo' : 'acabrerrob@educacion.navarra.es',
                                'aprobado' : True}}
                                ,
                {'11111111A' : {'nombre' : 'martin',
                                'apellido' : 'robles',
                                'teléfono' : 661698954,
                                'correo' : 'mcabrerrob@educacion.navarra.es',
                                'aprobado' : True}}
                                ,
                {'33333333A' : {'nombre' : 'lore',
                                'apellido' : 'ipsum',
                                'teléfono' : 000000000,
                                'correo' : 'loreipsum@educacion.navarra.es',
                                'aprobado' : False}}]


option = input('Introduzca el número de opcion que desee:\n  (1) Añadir alumno/a\n  (2) Eliminar alumno/a\n  (3) Mostrar alumno/a\n  (4) Listar todo el alumnado\n  (5) Listar alumnado aprobado\n  (6) Terminar\n')

match option: 
    # case '1': 
    case '2':
        deletNIF = input('Introduzca el NIF a borrar: ')
        for index in studentsList :
            if index.get(deletNIF)  :
                studentsList.remove(index)
print(studentsList)
    # case '3':
    # case '4':
    # case '5':
    # case '6':











