from productos.decorator.IngredienteExtra import IngredienteExtra


class ToppingChocolate(IngredienteExtra):
    def __init__(self, producto):
        super().__init__(producto)
        self.descripcion_extra = "con topping de chocolate"
        self.costo_extra = 0.50

    def get_descripcion(self):
        return f"{self._producto.get_descripcion()}, {self.descripcion_extra}"

    def get_costo(self):
        return self._producto.get_costo() + self.costo_extra
