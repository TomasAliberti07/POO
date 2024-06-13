#Importamos todas las clases
from Producto import *
from Electronico import *
from  Alimento import *
# Crear instancias
producto1 = Producto("Remera", 20.500, 50)
electronico1 = Electronico("Teléfono", 350.250, 10, "Motorola", "G52")
alimento1 = Alimento("Galletas", 1.450, 100, "2024-06-30")

# Mostrar información de producto(clase padre),electronico(clase hija),alimento(clase hija)
producto1.mostrar_informacion()
print("\n")
electronico1.mostrar_informacion()
print("\n")
alimento1.mostrar_informacion()