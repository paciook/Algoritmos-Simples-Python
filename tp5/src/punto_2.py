def letras(palabra):
    """La función recibe una palabra y devuelve la letra 'A'
    si esta se encuentra más veces que la letra 'E', y viceversa.
    En el caso de que reciba más de una palabra o un caracter no
    válido, se devuelve '-1', y si la palabra tiene la misma cantidad
    de 'E' que de 'A', devuelve '0'"""

    # Primero seteo los valores iniciales de cada letra

    cantA = 0
    cantE = 0

    # Luego quito los espacio que pueden presentarse al principio
    # y/o al final de la palabra

    palabra = palabra.strip(" ")

    # Luego recorro cada letra de la palabra y sumo una unidad o no,
    # dependiendo del caso. A la vez verifico que los caracteres sean
    # válidos y que sea una sola palabra
    
    for letra in palabra:
        try:
            if letra == 'a' or letra == 'A':
                cantA += 1
            elif letra == 'e' or letra == 'E':
                cantE += 1
            elif letra == " " or isinstance(int(letra), int):
                print("Palabra no válida")
                return -1
        except ValueError:
            pass    
     
    # Por último verifico cual es la letra que más se repite, lo indico
    # en pantalla y lo devuelvo
    
    if cantA > cantE:
        print("A")
        return "A"
    elif cantA < cantE:
        print("E")
        return "E"
    elif cantA == cantE:
        print("Misma cantidad de ambas letras: ", cantA)
        return 0


if __name__ == "__main__":
    letras(input("Ingrese una palabra "))