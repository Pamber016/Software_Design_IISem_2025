from abc import ABC, abstractmethod


class Pedido(ABC):
    def __init__(self, id_pedido):
        self.id_pedido = id_pedido
        self.tipo = ""

    @abstractmethod
    async def procesar(self):
        pass

    def __str__(self):
        return f"{self.tipo} {self.id_pedido}"
