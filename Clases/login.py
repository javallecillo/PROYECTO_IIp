import os

# Importa la clase Instrucciones
from Instrucciones import Instrucciones

def verificar_acceso():
    # Muestra las instrucciones de inicio de sesión
    Instrucciones.ins_login()

    # Limpia la pantalla 
    os.system('cls' if os.name == 'nt' else 'clear')

    # Credenciales de acceso predeterminadas
    usuario = "admin"
    contrasenia = "admin123"
    contraseniaInversa = contrasenia[::-1]  # Invierte la contraseña
    acceso = False

    print("---INICIO DE SESION---\n")
    # Solicita al usuario ingresar sus credenciales
    usu = input("Ingrese el usuario: ")
    intento = input("Ingresa tu contraseña: ")
    intentoInverso = intento[::-1]  # Invierte la contraseña ingresada

    # Verifica si las credenciales ingresadas coinciden con las predeterminadas
    if usu == usuario and intento == contrasenia and intentoInverso == contraseniaInversa and contraseniaInversa[2::2] == intentoInverso[2::2]:
        acceso = True
        return acceso  # Retorna True si el acceso es exitoso

    else:
        # Informa al usuario que las credenciales son incorrectas
        print("\nUsuario o contraseña incorrectos.")

        # Opción para reintentar o cerrar el sistema
        pregunta = input("Presione Enter para intentar de nuevo, o X para cerrar el sistema: ").lower()

        if pregunta != "x":
            verificar_acceso()  # Llama recursivamente a la función para reintentar
        else:
            return exit()  # Cierra el sistema si el usuario ingresa 'x'