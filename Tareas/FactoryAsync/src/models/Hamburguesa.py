from models.Pedido import Pedido
import asyncio
import random


class Hamburguesa(Pedido):
    def __init__(self, id_pedido):
        super().__init__(id_pedido)
        self.tipo = "Hamburguesa"

    async def procesar(self):
        # Simular tiempo de preparación
        tiempo_preparacion = random.uniform(1, 3)
        await asyncio.sleep(tiempo_preparacion)
        return f"Hamburguesa {self.id_pedido} preparada"
