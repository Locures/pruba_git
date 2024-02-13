class Cliente:
    #atributo de clase
    edad_adulto = 18
    
    #constructor
    def __init__(self, nombre, edad, ubicacion, ingresos):
        self.nombre = nombre
        self.edad = edad
        self.ubicacion = ubicacion
        self.ingresos = ingresos
    # str
    def __str__(self):
        return f' El cliente {self.nombre} tiene {self.edad}, vive en {self.ubicacion} y gana ${self.ingresos}'
    # metodo 1
    def cliente_mayor(self):
        if self.edad < Cliente.edad_adulto:
            return print('No puede realizar ninguna compra')
        else:
            return print('Puede realizar compras')
    #metodo 2
    def rango_de_entrega(self):
        if self.ubicacion == "CABA" or self.ubicacion ==  "Ciudad de Buenos Aires":
            return print('La compra llegará en 1 día')
        else:
            return print('Fuera del rango de entregas')