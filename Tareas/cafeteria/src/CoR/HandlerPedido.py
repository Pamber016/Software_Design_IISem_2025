from abc import ABC, abstractmethod
from typing import Optional
from CoR.ItemPedido import ItemPedido

# Handler base
class HandlerPedido(ABC):
    def __init__(self):
        self._siguiente: Optional['HandlerPedido'] = None
    
    def set_siguiente(self, siguiente: 'HandlerPedido') -> 'HandlerPedido':
        self._siguiente = siguiente
        return siguiente
    
    @abstractmethod
    def manejar(self, item: ItemPedido) -> bool:
        pass
