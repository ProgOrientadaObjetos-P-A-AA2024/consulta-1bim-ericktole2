class Rectangulo:
    def __init__(self, longitud, ancho):
    
       ##Constructor de la clase Rectangulo.

    
        self.longitud = longitud
        self.ancho = ancho

    def area(self):
        ##Calcula el área del rectángulo.
        ## se puede hacer de varias formas , una de ellas es dando valor a una variable 
        #y retordando esa variable  de otra manera seria reportar la operacion en si , 
        #funciona de la misma manera 
        return self.longitud * self.ancho

    def perimetro(self):
        ## Calcula el perímetro del rectángulo.

        return 2 * (self.longitud + self.ancho)

# Creando una instancia de la clase Rectangulo
# de aca tomara los datos el costructor para poder ejecuarce, estos se peuden 
#cambiar ya sea llamando por teclado y enviando las variables 
mi_rectangulo = Rectangulo(5, 3)

# Mostrando el área y el perímetro del rectángulo
print("Área del rectángulo:", mi_rectangulo.area()) 
 # Salida: Área del rectángulo: 15
print("Perímetro del rectángulo:", mi_rectangulo.perimetro())  
# Salida: Perímetro del rectángulo: 16
