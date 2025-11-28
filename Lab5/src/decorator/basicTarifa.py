from tarifa import tarifa


class basicTarifa(tarifa):
    def __init__(self, tarifa_base):
        self._tarifa_base = tarifa_base

    def calcular_tarifa(self):
        return self._tarifa_base
