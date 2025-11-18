from typing import List
from CoR.NotificadorHandler import NotificadorHandler
from CoR.BaristaHandler import BaristaHandler
from CoR.PasteleroHandler import PasteleroHandler
from CoR.ItemPedido import ItemPedido
from observer.Subject import Subject
from productos.Producto import Producto
from observer.Cliente import Cliente


class SistemaPedidos(Subject):
    def __init__(self):
        super().__init__()
        self.pedidos: List[ItemPedido] = []
        # Configurar Chain of Responsibility
        self.barista = BaristaHandler()
        self.pastelero = PasteleroHandler()
        self.notificador = NotificadorHandler(self)

        self.barista.set_siguiente(self.pastelero)
        self.pastelero.set_siguiente(self.notificador)

    def agregar_pedido(self, producto: Producto, cliente: Cliente):
        item = ItemPedido(producto, cliente)
        self.pedidos.append(item)
        self.agregar_observador(cliente)
        print(f"Cliente: {cliente.nombre}")
        print(f"Ordena un {producto.get_descripcion()}")

    def procesar_pedidos(self):
        print("\n--- Procesando pedidos ---")
        for pedido in self.pedidos:
            self.barista.manejar(pedido)

    def notificar_cliente(self, cliente: Cliente, mensaje: str):
        cliente.actualizar(mensaje)
