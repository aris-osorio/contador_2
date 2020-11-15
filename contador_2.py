import re
from unidecode import unidecode

class archivo:
    def __init__(self, nombre):
        self.nombre = nombre
        try:
            self.archivo = open(nombre,  encoding="utf8")
        except:
            print("Error al procesar archivo")

def main():
    nombre = input("nombre o direccion de libro: ")
    cadena = archivo(nombre)
    print(cadena)
   
if  __name__ == "__main__":
    main()