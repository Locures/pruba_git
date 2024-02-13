# Crea un programa que solicite un número entero al usuario y determine si es un número negativo, 
# positivo o igual a cero. En caso de ser positivo, verifica si es par o impar.

num_clave = int(input("ingrese un numero: "))
if num_clave > 0:
    if num_clave %2 ==0:
        print("el numero es positivo y par")
    else:
        print ("el numero es posito e impar")
else:
    print ("el numero es negativo") 
    