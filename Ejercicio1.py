currencyDict = {'euro' : '€', 'dollar' : '$', 'yen' : '¥'}


badge = input ('Introduzca una divisa: ').lower()


if badge in currencyDict :
    print(currencyDict.get(badge))
else :
    print('Su divisa no se encuentra en el diccionario.')