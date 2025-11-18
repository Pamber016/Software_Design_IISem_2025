from productos.Producto import Producto

class Croissant(Producto):
    def get_descripcion(self) -> str:
        return "Croissant"
    
    def get_precio(self) -> float:
        return 1500.0
