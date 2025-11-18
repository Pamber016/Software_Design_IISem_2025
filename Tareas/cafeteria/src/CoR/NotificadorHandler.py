from CoR.HandlerPedido import HandlerPedido
from CoR.ItemPedido import ItemPedido
# from modelo.SistemaPedidos import SistemaPedidos

class NotificadorHandler(HandlerPedido):
    def __init__(self, sistema_pedidos: 'SistemaPedidos'):
        super().__init__()
        self.sistema_pedidos = sistema_pedidos
    
    def manejar(self, item: ItemPedido) -> bool:
        if item.preparado:
            self.sistema_pedidos.notificar_cliente(item.cliente, f"Su pedido '{item.producto.get_descripcion()}' está listo!")
            return True
        elif self._siguiente:
            return self._siguiente.manejar(item)
        return False