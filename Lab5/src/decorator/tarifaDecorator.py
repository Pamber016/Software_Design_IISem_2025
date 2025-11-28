from tarifa import tarifa


class tarifaDecorator(tarifa):
    def __init__(self, tarifa_decorada):
        self._tarifa_decorada = tarifa_decorada

    def calcular_tarifa(self):
        return self._tarifa_decorada.calcular_tarifa()
