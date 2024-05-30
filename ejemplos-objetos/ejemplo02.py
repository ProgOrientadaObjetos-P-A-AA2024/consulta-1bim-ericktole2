class Pelicula:
    def __init__(self, titulo, ano_estreno):
        self.titulo = titulo
        self.ano_estreno = ano_estreno

# Crear instancias de la clase Pelicula para cada película de Star Wars
star_wars = [
    Pelicula("Star Wars: Episodio IV - Una nueva esperanza", 1977),
    Pelicula("Star Wars: Episodio IX - El ascenso de Skywalker", 2019)
]

# Mostrar solo el año de estreno de cada película
for pelicula in star_wars:
    print(f"Pelicula: {pelicula.titulo} con ano de estreno: {pelicula.ano_estreno}")
