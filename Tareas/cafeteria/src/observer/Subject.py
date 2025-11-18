from abc import ABC
from typing import List
from observer.Observer import Observador


# Subject
class Subject(ABC):
    def __init__(self):
        self._observadores: List[Observador] = []

    def agregar_observador(self, observador: Observador):
        self._observadores.append(observador)

    def eliminar_observador(self, observador: Observador):
        self._observadores.remove(observador)

    def notificar_observadores(self, mensaje: str):
        for observador in self._observadores:
            observador.actualizar(mensaje)
