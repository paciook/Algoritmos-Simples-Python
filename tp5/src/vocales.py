def devuelveVocales(palabra):
    """La función recibe una palabra y devuelve la cantidad
    de cada vocal que hay en una lista del formato:
    [A, E, I, O, U]. En el caso de ingresa una palabra no
    válida o más de una palabra, se devuelve '0'"""

    # Primero instancio una lista con 5 valores = 0

    vocales = [0, 0, 0, 0, 0]

    # Luego quito los espacios que se puedan presentar
    # en la palabra y verifico que sea una palabra válida.
    # A la vez, recorro la palabra en busca de vocales

    palabra = palabra.strip(" ")
    for letra in palabra:
        try:
            if letra == " " or isinstance(float(letra), float):
                return 0
        except:
            pass
        if letra.upper() == "A":
            vocales[0] += 1
        if letra.upper() == "E":
            vocales[1] += 1
        if letra.upper() == "I":
            vocales[2] += 1
        if letra.upper() == "O":
            vocales[3] += 1
        if letra.upper() == "U":
            vocales[4] += 1 

    # Muestro los resultados en pantalla 
    
    print("A: ", vocales[0])
    print("E: ", vocales[1])
    print("I: ", vocales[2])
    print("O: ", vocales[3])
    print("U: ", vocales[4])

    # Devuelvo los resultados

    return vocales








if __name__ == "__main__":
    devuelveVocales(input("Ingrese una palabra"))