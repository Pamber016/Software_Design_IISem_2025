from Libro import Libro
class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, titulo, autor, genero, paginas, anio):
        l = Libro(titulo, autor, genero, paginas, anio)
        self.libros.append(l)
        print("Libro agregado!")
        return l

    def solicitar_datos_libro(self):
        titulo = input("Título: ")
        autor = input("Autor: ")
        genero = input("Género (novela/ciencia/historia): ").lower()
        paginas = self.solicitar_numero("Número de páginas: ")
        anio = self.solicitar_numero("Año de publicación: ")
        return titulo, autor, genero, paginas, anio

    def solicitar_numero(self, mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Error: Debe ingresar un número válido.")

    def generar_reporte(self):
        self.imprimir_libros()
        self.mostrar_estadisticas()

    def imprimir_libros(self):
        for libro in self.libros:
            libro.imprimir_datos()

    def mostrar_estadisticas(self):
        total = len(self.libros)
        antiguos = self.calcular_antiguos()
        disponibles = self.calcular_disponibles()
        promedio_popularidad = self.calcular_promedio_popularidad(total)

        print("\nREPORTE BIBLIOTECA:")
        print(f"Total libros: {total}")
        print(f"Disponibles: {disponibles}")
        print(f"Antiguos: {antiguos}")
        print(f"Promedio de popularidad: {promedio_popularidad}")

    def calcular_antiguos(self):
        return sum(1 for libro in self.libros if libro.es_antiguo())

    def calcular_disponibles(self):
        return sum(1 for libro in self.libros if libro.disponible)

    def calcular_promedio_popularidad(self,total):
        popularidad_total = sum(libro.calcular_popularidad() \
            for libro in self.libros)
        return popularidad_total / total if total > 0 else 0
