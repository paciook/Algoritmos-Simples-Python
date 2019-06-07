import hashlib as HASH


def verificaContrasena(contrasena):
    
    """La función recibe una palabra y verifica si es la contraseña
    correcta """

    # Primero convierto la contraseña a un conjunto de 
    # bytes para poder ser pasada por las funciones de hash

    contrasena = bytes(contrasena, encoding='utf-8')
    
    # Luego paso la palabra por tres funciones de hash distintas
    
    sha1 = (HASH.sha1(contrasena)).hexdigest()
    sha256 = (HASH.sha256(contrasena)).hexdigest()
    sha512 = (HASH.sha512(contrasena)).hexdigest()
    
    # Luego meto los tres 'hashes' en una tupla para un uso más
    # cómodo
    
    contrasena = (sha1, sha256, sha512)

    # Seteo el inicio de mi índice

    indice = -1
    
    # Abro el archivo para verificar los 'hashes'

    hashs = open("HASH")

    # Recorro con un ciclo for cada línea del archivo y
    # verifico que los códigos coincidan

    for linea in hashs:
        
        # Aumento el índice cada vez que cambio de línea
        # para que compare el hash siguiente
        
        indice += 1

        # Comparo la línea quitándole las bajadas de línea de los
        # extremos, y si alguno de los códigos no coincide, se devuelve
        # 'False' y se indica en pantalla

        if linea.strip('\n') != contrasena[indice]:
            print("Contraseña incorrecta, capo")
            return False
    print("Etzelente")

if __name__ == "__main__":
    verificaContrasena(input("Contraseña: "))
