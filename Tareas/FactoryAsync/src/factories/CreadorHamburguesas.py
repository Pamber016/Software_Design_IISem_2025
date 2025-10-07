from factories.CreadorPedidos import CreadorPedidos
from models.Hamburguesa import Hamburguesa


class CreadorHamburguesas(CreadorPedidos):
    def crear_pedido(self, id_pedido):
        return Hamburguesa(id_pedido)
