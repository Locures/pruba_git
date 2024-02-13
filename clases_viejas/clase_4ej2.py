# Ubica la palabra
# Escribe un programa que tome una lista de nombres ingresados por el usuario separados por un espacio y los liste 
# mostrando su ubicación

nombres = input("ingrese dos nombres separados por un espacio: ").split()

for indice, valor in enumerate(nombres):
    print(f"Nombre{indice + 1}: {valor}")