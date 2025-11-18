from productos.Producto import Producto


class TeVerde(Producto):
    def get_descripcion(self) -> str:
        return "Té Verde"

    def get_precio(self) -> float:
        return 1500.0
