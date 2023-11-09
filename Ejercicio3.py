shoppingDic = {'Pan' : 1.40, 'Huevos' : 2.30, 'Cebolla' : 0.85, 'Aceite' : 4.35}


product = input('Introduzca el producto que desee: ').title()
cuantitie = float(input('Introduzca la cantidad que desee: '))


if product in shoppingDic :
    productPrice = shoppingDic.get(product) * cuantitie
    print (productPrice)
else :
    print('Su producto no se encuentra en el diccionario.')