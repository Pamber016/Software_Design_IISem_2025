class Libro:
    def __init__(self, titulo, autor, genero, paginas, anio_publicacion,
    disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero # 'novela', 'ciencia', 'historia'
        self.paginas = paginas
        self.anio_publicacion = anio_publicacion
        self.disponible = disponible

    def calcular_popularidad(self):
        lista_generos = {
            'novela': {'base': 50, 'divisor': 10},
            'ciencia': {'base': 70, 'divisor': 5},
            'historia': {'base': 40, 'divisor': 8}
        }

        valor = lista_generos.get(self.genero, {'base': 10, 'divisor': 1})
        
        popularidad = valor['base'] + (self.paginas / valor['divisor'])
        return popularidad

    def es_antiguo(self):
        if self.anio_publicacion < 1980:
            return True
        else:
            return False

    def imprimir_datos(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Género: {self.genero}")
        print(f"Páginas: {self.paginas}")
        print(f"Año: {self.anio_publicacion}")
        print(f"Disponible: {'Sí' if self.disponible else 'No'}")
        print(f"Popularidad: {self.calcular_popularidad()}")
        print(f"Es antiguo: {'Sí' if self.es_antiguo() else 'No'}")
        print("------------------------")