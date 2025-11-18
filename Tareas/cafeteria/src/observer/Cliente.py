from observer.Observer import Observador

# Cliente
class Cliente(Observador):
    def __init__(self, nombre: str):
        self.nombre = nombre

    def actualizar(self, mensaje: str):
        print(f"Notificación para {self.nombre}: {mensaje}")