import hashlib as HASH


def verificaContrasena(contrasena):
    contrasena = bytes(contrasena, encoding='utf-8')
    hashs = open("HASH")
    sha1 = (HASH.sha1(contrasena)).hexdigest()
    sha256 = (HASH.sha256(contrasena)).hexdigest()
    sha512 = (HASH.sha512(contrasena)).hexdigest()
    contrasena = (sha1, sha256, sha512)
    indice = -1
    for linea in hashs:
        indice += 1
        if linea.strip('\n') != contrasena[indice]:
            print("Contraseña incorrecta, capo")
            return False
    print("Etzelente")

if __name__ == "__main__":
    verificaContrasena(input("Contraseña: "))
