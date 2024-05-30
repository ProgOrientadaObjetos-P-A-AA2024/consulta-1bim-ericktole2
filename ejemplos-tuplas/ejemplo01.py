# Crear una tupla de números
tupla_numeros = (1, 2, 3, 4, 5)
print("Tupla de números:", tupla_numeros)

# Crear una tupla de strings
tupla_strings = ("manzana", "banana", "cereza")
print("Tupla de strings:", tupla_strings)

# Crear una tupla mixta
tupla_mixta = (1, "dos", 3.0, True)
print("Tupla mixta:", tupla_mixta)

# Acceder al primer elemento de la tupla
primer_elemento = tupla_numeros[0]
print("Primer elemento de la tupla de números:", primer_elemento)

# Acceder al último elemento de la tupla
ultimo_elemento = tupla_strings[-1]
print("Último elemento de la tupla de strings:", ultimo_elemento)

# Concatenar dos tuplas
tupla_concatenada = tupla_numeros + tupla_strings
print("Tupla concatenada:", tupla_concatenada)

# Desempaquetar una tupla
a, b, c = tupla_strings
print("Desempaquetado de tupla:", a, b, c)

# Iterar sobre una tupla
for elemento in tupla_mixta:
    print(elemento)
