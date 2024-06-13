from Producto import *#Importo la clase Padre
class Electronico(Producto):#Creo la clase Elecctronico
    def __init__(self, nombre, precio, cantidad, marca, modelo):
        super().__init__(nombre, precio, cantidad)
        self.marca = marca
        self.modelo = modelo
 #Funcion para mostrar la informacion de electronico
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
