import TotalDepartamentos
import os

# clase de opciones del programa
class opcionesMenu:
    def mostrar_depto_edad(self):
        print("Ingrese su número de cédula")
        cedula = input()
        if len(cedula) >= 8:
            try:
                ano = int(cedula[4:8])
                departamento = str(cedula[0:4])
                edad = 2024 - ano
                if departamento in TotalDepartamentos.Departamentos and ano <= 2024:
                    print("Su departamento es:", TotalDepartamentos.Departamentos[departamento], "\nSu edad es:", edad)
                else:
                    print("Algo salió mal, vuelve a intentarlo")
            except ValueError:
                print("La cédula debe contener números válidos para el año y el departamento")

    def mostrar_municipios_cedula(self):
        print("Ingrese su numero de cedula")
        cedula = input()
        municipio = str(cedula[0:2])
        print("Los municipios de su departamento son:")
        if municipio == "01":
            for clave, valor in TotalDepartamentos.Atlantida.items():
                print(clave, valor)
        elif municipio == "02":
                for clave, valor in TotalDepartamentos.Colon.items():
                    print(clave, valor)
        elif municipio == "03":
                for clave, valor in TotalDepartamentos.Comayagua.items():
                    print(clave, valor)        
        elif municipio == "04":
                for clave, valor in TotalDepartamentos.Copan.items():
                    print(clave, valor)
        elif municipio == "05":
                for clave, valor in TotalDepartamentos.Cortes.items():
                    print(clave, valor)
        elif municipio == "06":
                for clave, valor in TotalDepartamentos.Choluteca.items():
                    print(clave, valor)
        elif municipio == "07":
                for clave, valor in TotalDepartamentos.Paraiso.items():
                    print(clave, valor)
        elif municipio == "08":
                for clave, valor in TotalDepartamentos.Morazan.items():
                    print(clave, valor)
        elif municipio == "09":
                for clave, valor in TotalDepartamentos.Gracias.items():
                    print(clave, valor)
        elif municipio == "10":
                for clave, valor in TotalDepartamentos.Intibuca.items():
                    print(clave, valor)
        elif municipio == "11":
                for clave, valor in TotalDepartamentos.Isla.items():
                    print(clave, valor)
        elif municipio == "12":
                for clave, valor in TotalDepartamentos.Paz.items():
                    print(clave, valor)
        elif municipio == "13":
                for clave, valor in TotalDepartamentos.Lempira.items():
                    print(clave, valor)
        elif municipio == "14":
                for clave, valor in TotalDepartamentos.Ocotepeque.items():
                    print(clave, valor)
        elif municipio == "15":
                for clave, valor in TotalDepartamentos.Olancho.items():
                    print(clave, valor)
        elif municipio == "16":
                for clave, valor in TotalDepartamentos.Santa.items():
                    print(clave, valor)
        elif municipio == "17":
                for clave, valor in TotalDepartamentos.Valle.items():
                    print(clave, valor)
        elif municipio == "18":
                for clave, valor in TotalDepartamentos.Yoro.items():
                    print(clave, valor)


    # definir decision del menu
    def opcion(self, opcion):
        if opcion == 1:
            self.mostrar_depto_edad()
        elif opcion == 2:
            self.mostrar_municipios_cedula()

    