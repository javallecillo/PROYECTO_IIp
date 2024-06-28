import os
import TotalDepartamentos 

class Deseos:
    def __init__(self, TotalDepartamentos):
        self.TotalDepartamentos = TotalDepartamentos

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def procesar_deseo(self, deseo):
        self.limpiar_pantalla()
        if deseo == 1:
            self.procesar_cedula_para_departamento_y_edad()
        elif deseo == 2:
            self.procesar_cedula_para_municipios()

    def procesar_cedula_para_departamento_y_edad(self):
        print("Ingrese su número de cédula")
        cedula = input()
        if len(cedula) >= 8:
            try:
                ano = int(cedula[4:8])
                departamento = str(cedula[0:4])
                edad = 2024 - ano
                if departamento in self.TotalDepartamentos.Departamentos and ano <= 2024:
                    print("Su departamento es:", self.TotalDepartamentos.Departamentos[departamento], "\nSu edad es:", edad)
                else:
                    print("Algo salió mal, vuelve a intentarlo")
            except ValueError:
                print("La cédula debe contener números válidos para el año y el departamento")
        self.solicitar_nueva_accion()

    def procesar_cedula_para_municipios(self):
        print("Ingrese su número de cédula")
        cedula = input()
        municipio = str(cedula[0:2])
        print("Los municipios de su departamento son:")
        municipios = getattr(self.TotalDepartamentos, municipio, None)
        if municipios:
            for clave, valor in municipios.items():
                print(clave, valor)
        else:
            print("Código de municipio no encontrado.")
        self.solicitar_nueva_accion()

    def solicitar_nueva_accion(self):
        print("Desea Hacer otra cosa? S/N")
        opcion = input()
        self.limpiar_pantalla()


