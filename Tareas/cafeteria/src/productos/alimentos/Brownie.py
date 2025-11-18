from productos.Producto import Producto

class Brownie(Producto):
    def get_descripcion(self) -> str:
        return "Brownie"
    
    def get_precio(self) -> float:
        return 1500.0
