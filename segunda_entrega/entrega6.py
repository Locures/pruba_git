# Definimos diccionario general Base_de_usuarios

Base_de_usuarios = {}

# funcion para agregar usuarios y contraseña - opcion 1

def registro ():
    usuario = input("Elija un nombre usuario: ")
    while usuario in Base_de_usuarios:
            usuario = input("Nombre de usuario no disponible, ingrese otro: ")       
    contraseña = input("Elija una contraseña: ")
    Base_de_usuarios[usuario] = contraseña
    print("registrado")

# funcion para comprobar usuario y contraseña - login

def loguear():
    usuario = input("Ingrese su nombre de usuario: ")
    while usuario not in Base_de_usuarios:
        print("Usuario no registrado.")
        print("1. Ingresar usuario nuevamente")
        print("2. Salir")
        opcion_loguin_erroneo = input("Elija opcion")
        if opcion_loguin_erroneo == "1":
            usuario = input("Ingrese su nombre de usuario: ")
        if opcion_loguin_erroneo == "2":
            break 
        else:
            print("Elija opcion del menu login")
    contraseña = input("Ingrese su contraseña: ")
    if Base_de_usuarios[usuario] == contraseña:
            print("Inicio de sesión correcto.")
    else:
            print("Contraseña incorrecta.")

# funcion para mostrar la base de datos - opcion 3

def imprimir_base ():
    while True:
        print("1. Mostrar todos los usuarios")
        print("2. Mostrar todos las contraseñas")
        print("3. Mostrar los usuarios y contraseñas")
        print("4. Salir")
        opcion_base = input("ingrese opcion: ")
    
        if opcion_base == "1":
            for usuario in Base_de_usuarios.keys():
                print(f'Usuario: {usuario}')
        elif opcion_base == "2":
            for contraseña in Base_de_usuarios.values():
                print(f'Contraseña: {contraseña}')
        elif opcion_base == "3":
            for usuario, contraseña in Base_de_usuarios.items():
                print(f'Usuario: {usuario}')
                print(f'Contraseña: {contraseña}')
        elif opcion_base == "4":
            break
        else:
            print("Elija una opcion del menu de revisar base")
    

# un menu registrarse, loguear, revisar y salir

while True:
    print("1. Nuevo usuario")
    print("2. Login")
    print("3. Revisar base")
    print("4. Salir")
    opcion = input("ingrese opcion: ")
                 
    if opcion == "1":
            registro()
    elif opcion == "2":
        loguear()
    elif opcion == "3":
        imprimir_base()
    elif opcion == "4":
        break
    else:
        print("Elija una opcion del menu")
        

    

