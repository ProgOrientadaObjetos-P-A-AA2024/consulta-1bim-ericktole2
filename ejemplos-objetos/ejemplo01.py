class Perro:
    def __init__(self, nombre, raza, fecha_nacimiento):
        # Constuctor de la clase perro donde llegan 3 datos String y entero 
        self.nombre = nombre
        self.raza = raza
        self.fecha_nacimiento = fecha_nacimiento
        # Asignamos el valor a las variables de los datos pedidos 

# Creamos dos objetos de la clase Perro
perro1 = Perro("Max", "Labrador", "2018-05-15")
perro2 = Perro("Bella", "Poodle", "2020-10-20")

# Mostramos información sobre los perros
print(f"{perro1.nombre} es un {perro1.raza} y nació el {perro1.fecha_nacimiento}")
print(f"{perro2.nombre} es un {perro2.raza} y nació el {perro2.fecha_nacimiento}")
