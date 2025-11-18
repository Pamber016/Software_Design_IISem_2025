from productos.Producto import Producto

class Cafe(Producto):
    def get_descripcion(self) -> str:
        return "Cafe"
    
    def get_precio(self) -> float:
        return 1500.0
