def consonantes(frase):
    """La función recibe una frase, quita las vocales y la devuelve"""

    # Reemplazo las vocales con espacios vacíos

    frase = frase.replace('a', "")
    frase = frase.replace('A', "")
    frase = frase.replace('E', "")
    frase = frase.replace('e', "")
    frase = frase.replace('I', "")
    frase = frase.replace('i', "")
    frase = frase.replace('o', "")
    frase = frase.replace('O', "")
    frase = frase.replace('u', "")
    frase = frase.replace('U', "")

    print (frase)
    return frase


def vocales(frase):
    """La función recibe una frase, quita las consonantes y la devuelve"""

    # Recorro una lista y sólo guardo en otra variable lo que necesite
    
    devolucion = ""
    for letra in frase:
        eslower = False
        if letra.islower() == False:
            letra = letra.lower()
        else:
            eslower == True

        if letra == 'a':
            if eslower == True:
                devolucion += 'a'
            else:
                devolucion += 'A'
        if letra == 'e':
            if eslower == True:
                devolucion += 'e'
            else:
                devolucion += 'E'
        if letra == 'i':
            if eslower == True:
                devolucion += 'i'
            else:
                devolucion += 'I'
        if letra == 'o':
            if eslower == True:
                devolucion += 'o'
            else:
                devolucion += 'O'
        if letra == 'u':
            if eslower == True:
                devolucion += 'u'
            else:
                devolucion += 'U'
        if letra == " ":
            devolucion += " "
    print(devolucion)
    return devolucion

def sigVocal(frase):
    """La funcion recibe una frase y devuelve la misma frase pero cada vocal
    reemplazada con su siguiente"""
    letras = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

    for x in range(5):
        frase = frase.replace(letras[x], letras[x+2])
        frase = frase.replace(letras[8], letras[0])
        frase = frase.replace(letras[9], letras[1])
    print(frase)
    return frase

sigVocal("muRcIelAgo")

def palindromo(frase):
    """La función recibe una frase y la compara con su reverso, de ser
    iguales devuelve True, y si no, False"""

    # Comparo la frase sin espacios y en minúsculas con su reverso
    # y devuelvo los resultados

    frase = frase.replace(' ', '')
    frase = frase.lower()

    if frase[::-1] == frase:
        print("Es palíndromo")
        return True
    else:
        print("No es palíndromo")
        return False
    

