# Escribir un programa que pregunte al usuario su nombre, edad,
# dirección y teléfono y lo guarde en un diccionario. Después 
# debe mostrar por pantalla el mensaje “<nombre> tiene <edad> 
# años, vive en <dirección> y su número de teléfono es <teléfono>”.
# dictionary[clave] = valor : Añade al diccionario dictionary 
# el par formado por la clave clave y el valor valor.

personalDict = {}

name = input('Introduzca su nombre: ')
age = int (input('Introduzca su edad: '))
address = input('Introduzca su dirección: ')
phoneNum = int (input('Introduzca su número de teléfono: '))

personalDict['nombre'] = name
personalDict['edad'] = age
personalDict['dirección'] = address
personalDict['teléfono'] = phoneNum

print(personalDict)