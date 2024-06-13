from Producto import *#Importo la clase Padre
class Alimento(Producto):#Creo la clase Alimento 
    def __init__(self, nombre, precio, cantidad, fecha_expiracion):
        super().__init__(nombre, precio, cantidad)
        self.fecha_expiracion = fecha_expiracion
  #Funcion para mostrar informacion de Alimento 
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Fecha de expiración: {self.fecha_expiracion}")
