# Inventario

# Imagina que estás administrando un pequeño almacén y deseas realizar un seguimiento de los productos en tu inventario. 
# Escribe un programa que te permita ingresar el nombre y la cantidad de varios productos. 
# Utiliza un bucle para recorrer los productos y mostrar su nombre y cantidad.
# Al final, muestra el total de productos en el inventario.

inventario = {}

num_productos = int(input("Ingresa la cantidad de productos en el inventario a cargar: "))

# el _ se suele utilizar para definir variables que no se van a utilizar como
# en este caso que no se utiliza su valor dentro del for
for _ in range(num_productos):
    nombre = input("Ingresa el nombre del producto: ")
    cantidad = int(input(f"Ingresa la cantidad de {nombre}: "))
    inventario[nombre] = cantidad

print("\nInventario:")
total_productos = 0

for producto, cantidad in inventario.items():
    print(f"{producto}: {cantidad}")
    total_productos += cantidad

print("\nTotal de productos en el inventario:", total_productos)
     