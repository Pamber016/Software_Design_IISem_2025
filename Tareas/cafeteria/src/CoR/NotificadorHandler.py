from CoR.HandlerPedido import HandlerPedido
from CoR.ItemPedido import ItemPedido

class NotificadorHandler(HandlerPedido):
    def __init__(self, sistema_pedidos: "SistemaPedidos"):
        super().__init__()
        self.sistema_pedidos = sistema_pedidos

    def manejar(self, item: ItemPedido) -> bool:
            if item.preparado:
                mensaje = f"Su pedido '{item.producto.get_descripcion()}' está listo!"
                self.sistema_pedidos.notificar_cliente(item.cliente, mensaje)
                return True
            return False