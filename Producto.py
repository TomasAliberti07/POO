class Producto:#Creo la clase Padre
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
  #Funcion para mostrar informacion de producto
    def mostrar_informacion(self):
        print(f"Producto: {self.nombre}")
        print(f"Precio: {self.precio}")
        print(f"Cantidad disponible: {self.cantidad} ")

