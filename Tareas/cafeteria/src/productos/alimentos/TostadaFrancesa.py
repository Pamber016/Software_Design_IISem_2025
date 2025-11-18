from productos.Producto import Producto

class TostadaFrancesa(Producto):
    def get_descripcion(self) -> str:
        return "Tostada Francesa"
    
    def get_precio(self) -> float:
        return 1500.0
