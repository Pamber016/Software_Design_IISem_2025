from productos.Producto import Producto
from observer.Cliente import Cliente


# Item del pedido
class ItemPedido:
    def __init__(self, producto: Producto, cliente: Cliente):
        self.producto = producto
        self.cliente = cliente
        self.preparado = False

    def marcar_preparado(self):
        self.preparado = True

    def __str__(self) -> str:
        return self.producto.get_descripcion()
