from productos.decorator.IngredienteExtra import IngredienteExtra


class RellenoCrema(IngredienteExtra):
    def __init__(self, producto):
        super().__init__(producto)
        self.descripcion_extra = "con relleno de crema"
        self.costo_extra = 0.85

    def get_descripcion(self):
        return f"{self._producto.get_descripcion()}, {self.descripcion_extra}"

    def get_precio(self):
        return self._producto.get_precio() + self.costo_extra
