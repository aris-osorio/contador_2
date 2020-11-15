import re
from unidecode import unidecode

class archivo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.archivo = open(nombre,  encoding="utf8")
    
    def obtener_cadena(self):
        cadena = self.archivo.read()
        self.archivo.close()
        return cadena
    
    def crear_lista(self, cadena):
        cadena = cadena.replace("\n" , " ")
        cadena = re.sub(r"[^A-Za-z0-9áéíóúüñÁÉÍÓÚÜÑ]+", " ", cadena)
        cadena = unidecode(cadena)
        cadena = cadena.lower()
        lista = cadena.split(" ")
        return lista
    
    def contar_palabras(self, lista):
        diccionario = {}
        for palabra in lista:
            if palabra in diccionario:
                diccionario[palabra] = diccionario.get(palabra) + 1
            else:
                diccionario[palabra] = 1
        return diccionario
    
    def top_diez(self, diccionario):
        tabla = "Top 10 palabras que mas se repiten en " + self.nombre + "\n"
        palabras_top = sorted(diccionario, key=diccionario.get, reverse=True)[ :10] 
        for palabras in palabras_top:
            tabla += palabras + " ---> " + str(diccionario[palabras]) + "\n"
        return tabla

def main():
    nombre = input("nombre o direccion de libro: ")
    documento = archivo(nombre)
    cadena = documento.obtener_cadena()
    lista = documento.crear_lista(cadena)
    diccionario = documento.contar_palabras(lista)
    tabla = documento.top_diez(diccionario)
    print(tabla)       
   
if  __name__ == "__main__":
    main()