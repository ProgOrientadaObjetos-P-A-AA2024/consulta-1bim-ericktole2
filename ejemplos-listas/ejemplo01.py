# Creamos una lista de números
numeros = [1, 2, 3, 4, 5]

# Mostramos la lista
print("Lista de números:", numeros)  # Salida: Lista de números: [1, 2, 3, 4, 5]

# Accedemos al primer elemento de la lista (índice 0)
primer_numero = numeros[0]
print("Primer número:", primer_numero)  # Salida: Primer número: 1

# Accedemos al último elemento de la lista (índice -1)
ultimo_numero = numeros[-1]
print("Último número:", ultimo_numero)  # Salida: Último número: 5

# Modificamos un elemento de la lista
numeros[2] = 10
print("Lista modificada:", numeros)  # Salida: Lista modificada: [1, 2, 10, 4, 5]

# Añadimos un elemento al final de la lista
numeros.append(6)
print("Lista con un nuevo elemento:", numeros)  # Salida: Lista con un nuevo elemento: [1, 2, 10, 4, 5, 6]

# Eliminamos un elemento de la lista por su valor
numeros.remove(4)
print("Lista sin el número 4:", numeros)  # Salida: Lista sin el número 4: [1, 2, 10, 5, 6]

# Eliminamos un elemento de la lista por su índice
elemento_eliminado = numeros.pop(2)
print("Elemento eliminado:", elemento_eliminado)  # Salida: Elemento eliminado: 10
print("Lista después de eliminar el tercer elemento:", numeros)  

# Ordenamos la lista de forma ascendente
numeros.sort()
print("Lista ordenada:", numeros)  # Salida: Lista ordenada: [1, 2, 5, 6]

# Invertimos el orden de la lista
numeros.reverse()
print("Lista invertida:", numeros)  # Salida: Lista invertida: [6, 5, 2, 1]

# Creamos una lista vacía
lista_vacia = []
print("Lista vacía:", lista_vacia)  # Salida: Lista vacía: []
