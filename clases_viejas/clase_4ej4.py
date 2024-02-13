# Salteando palabras

# Escribe un programa que tome una lista de palabras ingresadas por el usuario. Luego, muestre cada palabra una por una.
# Si la palabra es "salir", finaliza el programa. Si la palabra es "omitir", se pasa a la siguiente iteración.
# Al final, si ninguna palabra fue "salir", muestra un mensaje avisando la situacion.

palabras = input("ingrese una serie de palabras separada por espacios: ").split()


for valor in palabras:
    if valor == "salir":
        break
    elif valor == "omitir":
        continue
    else:
        print(valor)
else:
    print("no se encontro palabra salir")