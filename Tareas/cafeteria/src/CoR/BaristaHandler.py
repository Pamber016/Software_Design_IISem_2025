from CoR.HandlerPedido import HandlerPedido
from CoR.ItemPedido import ItemPedido
from productos.bebidas import *
from productos.decorator.IngredienteExtra import IngredienteExtra
from productos.Producto import Producto


class BaristaHandler(HandlerPedido):
    def _es_bebida(self, producto: Producto) -> bool:
        if isinstance(producto, (Cafe, TeVerde, Espresso)):
            return True

        if isinstance(producto, IngredienteExtra):
            return self._es_bebida(producto._producto)

        return False

    def manejar(self, item: ItemPedido) -> bool:
        if self._es_bebida(item.producto):
            print(f"[Barista]: Preparo bebida: {item.producto.get_descripcion()}")
            item.marcar_preparado()
        if self._siguiente:
            return self._siguiente.manejar(item)
        return True
