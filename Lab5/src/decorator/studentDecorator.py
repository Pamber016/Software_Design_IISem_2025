from decorator.tarifaDecorator import tarifaDecorator


class studentDecorator(tarifaDecorator):
    def __init__(self, tarifa_decorada):
        super().__init__(tarifa_decorada)

    def calcular_tarifa(self):
        tarifa_original = self._tarifa_decorada.calcular_tarifa()
        descuento_estudiante = tarifa_original * 0.15
        return tarifa_original - descuento_estudiante
