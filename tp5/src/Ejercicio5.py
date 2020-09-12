def acronimo(frase):
    """La función recibe una frase y devuelve su acrónimo"""

    # Primero separo la frase en palabras

    frase = frase.split(" ")

    # Luego recojo la primer letra de cada palabra

    devolucion = ""
    for palabra in frase:
        devolucion += palabra[0].upper()
    print(devolucion)
    return devolucion


def primeraMayuscula(frase):
    """La función recibe una frase y la devuelve con cada primer letra de cada palabra
    en mayúscula"""

    # Modifico la frase para devolverla con cada primer letra en mayúscula

    print(frase.title())
    return frase.title()        


def palabrasConA(frase):
    """La función recibe una frase y devuelve todas las palabras empiezan con 'A'"""
    
    # Me aseguro que sea string por lo menos

    if !isinstance(frase, str):
        print("Dame un string, papito")
        return None

    # Primero instancio una variable con un string vacío

    devolucion = ""

    # Recorro cada palabra verificando su primer letra y guardo las que necesito

    frase = frase.split(" ")
    
    for palabra in frase:
        if palabra[0] == 'a' or palabra[0] == 'A':
            devolucion += palabra + ' '
    
    print(devolucion)
    return devolucion
