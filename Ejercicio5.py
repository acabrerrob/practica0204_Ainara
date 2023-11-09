dictionary = {}
string = ''

while True :
    words = input('Introduzca las palabras y sus traducciones de la siguiente manera: <palabra>:<traducción> , separando los terminos por comas: ').lower()

    if words == 'terminar' :
        break
    
    for index in words.split(',') :
        key, value = index.split(':')
        dictionary[key] = value

spanishSentence = input('Introduzca una frase en español a traducir: ')

spanishSentenceSpl = spanishSentence.split(' ')
for x in spanishSentenceSpl :
    if x in dictionary :
        string += dictionary[x] + ' '
    else :
        string += x + ' '
print (string)