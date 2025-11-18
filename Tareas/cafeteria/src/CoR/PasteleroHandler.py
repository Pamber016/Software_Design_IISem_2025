from CoR.HandlerPedido import HandlerPedido
from CoR.ItemPedido import ItemPedido
from productos.alimentos import *
from productos.decorator.IngredienteExtra import IngredienteExtra
from productos.Producto import Producto

class PasteleroHandler(HandlerPedido):
    def _es_alimento(self, producto: Producto) -> bool:
        if isinstance(producto, (Croissant, TostadaFrancesa, Brownie)):
            return True
        
        if isinstance(producto, IngredienteExtra):
            return self._es_alimento(producto._producto)
        
        return False
    
    def manejar(self, item: ItemPedido) -> bool:
        # Pastelero maneja alimentos
        if self._es_alimento(item.producto):
            print(f"[Pastelero]: Preparo alimento: {item.producto.get_descripcion()}")
            item.marcar_preparado()
            return True
        elif self._siguiente:
            return self._siguiente.manejar(item)
        return False