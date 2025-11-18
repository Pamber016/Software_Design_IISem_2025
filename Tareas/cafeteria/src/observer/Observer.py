from abc import ABC, abstractmethod


# Observer
class Observador(ABC):
    @abstractmethod
    def actualizar(self, mensaje: str):
        pass
