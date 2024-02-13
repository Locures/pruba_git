# Hay Tabla
# Escribe un programa que tome un número entero positivo ingresado por el usuario y muestre la tabla de multiplicar de ese número
# Repetir la solicitud al usuario de ingresar un nuevo número hasta que ingrese un cero.

while  True:
    num = int(input("Ingrese un numero: "))
    if num == 0:
        break
    for valor in range(1, 11):
        resultado = num * valor
        print(f"{num} * {valor} = {resultado}")