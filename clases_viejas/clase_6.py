# Clase 6 errores y objetos

# Que error genera

# Crear un programa que muestre un menu con 4 opciones y, segun la opcion elegida por el usuario, muestre el tipo de error
# que se generaria si se ejecutara ese codigo en python.  

# Usa las siguientes opciones:  
# 1. ‘Soy un string’ - 4
# 2. 4/0
# 3. prnt(‘Mostrando codigo’)
# 4. int(‘Quiero ser un numero’)

print("""Menu
1. ‘Soy un string’ - 4
2. 4/0
3. prnt(‘Mostrando codigo’)
4. int(‘Quiero ser un numero’)
""")

opcion = int(input("elija un numero: "))

try:
    if opcion == 1:
        "a" - 4
    elif opcion == 2:
        4/0
    elif opcion == 3:
        prnt("nde")
    elif opcion == 4:
        int('Quiero ser un numero')
    else:
        print("elija un numero dentro del menu")
except Exception as e:
    print("error del tipo:",type(e).__name__)
    