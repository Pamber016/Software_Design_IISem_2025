from productos.Producto import Producto


class Espresso(Producto):
    def get_descripcion(self) -> str:
        return "Café Doble Espresso"

    def get_precio(self) -> float:
        return 2500.0
