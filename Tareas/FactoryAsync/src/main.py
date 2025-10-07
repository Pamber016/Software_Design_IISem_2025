import random
from services.ServicioPedidos import ServicioPedidos
from factories.CreadorHamburguesas import CreadorHamburguesas
from factories.CreadorPizzas import CreadorPizzas

if __name__ == "__main__":
    servicio = ServicioPedidos(num_cocineros=2)

    creador_hamburguesas = CreadorHamburguesas()
    creador_pizzas = CreadorPizzas()

    # Crear y agregar pedidos aleatorios
    for i in range(6):
        if random.choice([True, False]):
            pedido = creador_hamburguesas.crear_pedido(i)
        else:
            pedido = creador_pizzas.crear_pedido(i)
        servicio.agregar_pedido(pedido)

    servicio.procesar_pedidos()
