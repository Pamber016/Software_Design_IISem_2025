# Producto base class
from abc import ABC, abstractmethod

class Producto(ABC):
    @abstractmethod
    def get_descripcion(self) -> str:
        pass

    @abstractmethod
    def get_precio(self) -> float:
        pass