import os
# Importa la clase Instrucciones
from Instrucciones import Instrucciones

# Función menu para mostrar las opciones al usuario
def menu():
    # Limpia la pantalla
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Muestra las opciones disponibles para el usuario
    print("---INGRESE LO QUE DESEA HACER---")
    print("1. Ver su departamento y municipios junto con su edad")
    print("2. Ver solo su municipio")
    print("3. Cerrar Sesion")

    # Solicita al usuario que ingrese el número de la opción deseada
    deseo = input("\nColoque el numero de la opcion(1, 2 o 3): ")

    # Retorna el número de la opción elegida por el usuario
    return deseo