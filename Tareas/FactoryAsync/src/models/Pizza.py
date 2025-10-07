from models.Pedido import Pedido
import asyncio
import random


class Pizza(Pedido):
    def __init__(self, id_pedido):
        super().__init__(id_pedido)
        self.tipo = "Pizza"

    async def procesar(self):
        # Simular tiempo de preparación
        tiempo_preparacion = random.uniform(2, 4)
        await asyncio.sleep(tiempo_preparacion)
        return f"Pizza {self.id_pedido} preparada"
