from factories.CreadorPedidos import CreadorPedidos
from models.Pizza import Pizza


class CreadorPizzas(CreadorPedidos):
    def crear_pedido(self, id_pedido):
        return Pizza(id_pedido)
