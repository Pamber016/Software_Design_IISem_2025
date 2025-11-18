# Decorator base class for extra ingredients
from productos.Producto import Producto

class IngredienteExtra(Producto):
    def __init__(self, producto: Producto):
        self._producto = producto

    def get_descripcion(self) -> str:
        return self._producto.get_descripcion()

    def get_precio(self) -> float:
        return self._producto.get_precio()