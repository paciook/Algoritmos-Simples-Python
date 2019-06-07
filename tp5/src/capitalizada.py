def capiONoCapi(frase1, frase2):
    """La función recibe una frase y devuelve True o False
    dependiendo de si la segunda frase es la versión capitalizada
    de la primera"""

    # Me aseguro que sea string por lo menos

    if isinstance(frase1, str) == False or isinstance(frase2, str) == False:
        print("Dame un string, papito")
        return None

    # Comparo la frase uno capitalizada con la frase dos y si son iguales
    # lo muestro en pantalla y devuelvo True. En el caso de no serlo,
    # también lo muestro en pantalla y devuelvo False

    if frase1.capitalize() == frase2:
        print("Es")
        return True
    else:
        print("No es")
        return False


if __name__ == "__main__":
    capiONoCapi(input("Ingrese la primer frase"), input("Y ahora la segunda"))