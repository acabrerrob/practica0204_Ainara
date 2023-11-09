dataList = ['nombre', 'edad', 'dirección', 'número']
personalDict = {}


for dataPosition in dataList :
    dataValue = input ('Introduzca su '+ dataPosition + ': ' )
    personalDict[dataPosition] = dataValue  


print (personalDict['nombre'], 'tiene ', personalDict['edad'], 'años, ', 'vive en ', personalDict['dirección'], 'y su número de teléfono es ', personalDict['número'])