import asyncio
import threading
from queue import Queue
import time


class ServicioPedidos:
    def __init__(self, num_cocineros=2):
        self.cola_pedidos = Queue()
        self.num_cocineros = num_cocineros
        self.cocineros = []
        self.pedidos_procesados = 0
        self.lock = threading.Lock()
        self.evento_todos_procesados = threading.Event()
        self.total_pedidos = 0

    def agregar_pedido(self, pedido):
        self.cola_pedidos.put(pedido)
        self.total_pedidos += 1

    def _cocinero_worker(self, id_cocinero):
        while True:
            try:
                pedido = self.cola_pedidos.get(timeout=1)

                print(
                    f"[COCINERO {id_cocinero}] Preparando pedido {pedido.id_pedido} ({pedido.tipo})")

                tiempo_preparacion = 2 if pedido.tipo == "Hamburguesa" else 3
                time.sleep(tiempo_preparacion)

                print(
                    f"[COCINERO {id_cocinero}] Pedido {pedido.id_pedido} listo: {pedido.tipo} {pedido.id_pedido} preparada")

                self.cola_pedidos.task_done()

                with self.lock:
                    self.pedidos_procesados += 1
                    if self.pedidos_procesados >= self.total_pedidos:
                        self.evento_todos_procesados.set()

            except:
                # Timeout ocurre cuando la cola está vacía por más de 1 segundo
                break

    def procesar_pedidos(self):
        print("Iniciando procesamiento de pedidos...")

        # Crear e iniciar cocineros (hilos)
        for i in range(self.num_cocineros):
            cocinero = threading.Thread(
                target=self._cocinero_worker, args=(i+1,)) # i+1 empieza en 1
            cocinero.daemon = True
            cocinero.start()
            self.cocineros.append(cocinero)

        # Esperar a que todos los pedidos sean procesados
        self.cola_pedidos.join()

        self.evento_todos_procesados.wait(timeout=5)

        print("[sistema] Todos los pedidos procesados")
