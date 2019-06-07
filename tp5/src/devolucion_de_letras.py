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
            letra.lower()
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
    pass


def palindromo(frase):
    pass

vocales("PAnchO cApO")