from abc import ABC, abstractmethod
from models.Pedido import Pedido


class CreadorPedidos(ABC):
    @abstractmethod
    def crear_pedido(self, id_pedido) -> Pedido:
        pass
