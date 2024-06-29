import os

def verificar_acceso():
    os.system('cls' if os.name == 'nt' else 'clear')

    usuario = "admin"
    contrasenia = "admin123"
    contraseniaInversa = contrasenia[::-1]
    acceso = False

    print("---INICIO DE SESION---\n")
    usu = input("Ingrese el usuario: ")
    intento = input("Ingresa tu contraseña: ")
    intentoInverso = intento[::-1]

    if usu == usuario and intento == contrasenia and intentoInverso == contraseniaInversa and contraseniaInversa[2::2] == intentoInverso[2::2]:
        acceso = True
        return acceso

    else:
        print("\nUsuario o contraseña incorrectos.")

        pregunta = input("Presione Enter para intentar de nuevo, o X para cerrar el programa: ").lower()

        while pregunta != "x":
            return verificar_acceso()