from abc import ABC, abstractmethod

# Interfaz de método de pago
class MetodoPago(ABC):
    @abstractmethod
    def pagar(self, monto: float) -> str:
        pass

# Implementaciones concretas de métodos de pago
class PayPal(MetodoPago):
    def pagar(self, monto: float) -> str:
        return f"Pago de ${monto} procesado con PayPal"

class TarjetaCredito(MetodoPago):
    def pagar(self, monto: float) -> str:
        return f"Pago de ${monto} procesado con Tarjeta de Crédito"

class TransferenciaBancaria(MetodoPago):
    def pagar(self, monto: float) -> str:
        return f"Pago de ${monto} procesado con Transferencia Bancaria"
    
class MetodoPagoNoSoportado(MetodoPago):
    def pagar(self, monto: float) -> str:
        return f"Pago de ${monto} deneago. Método de pago no soportado"

# Factory Method
class FabricaPagos:
    def crear_pago(self, tipo: str) -> MetodoPago:
        if tipo == "paypal":
            return PayPal()
        elif tipo == "tarjeta":
            return TarjetaCredito()
        elif tipo == "transferencia":
            return TransferenciaBancaria()
        else:
            return MetodoPagoNoSoportado()

# Uso en el sistema de reservas
class SistemaReservas:
    def __init__(self):
        self.factory = FabricaPagos()
    
    def reservar_vuelo(self, pasajero: str, monto: float, metodo_pago: str):
        # Factory crea el método de pago adecuado
        pago = self.factory.crear_pago(metodo_pago)
        
        # Procesar el pago
        resultado = pago.pagar(monto)
        
        print(f"Reserva para {pasajero}: {resultado}")

if __name__ == "__main__":
    sistema = SistemaReservas()
    
    # Reservas con diferentes métodos de pago
    sistema.reservar_vuelo("Amber Villarreal", 350.0, "paypal")
    sistema.reservar_vuelo("Pablo López", 420.0, "tarjeta") 
    sistema.reservar_vuelo("Jane Doe", 380.0, "transferencia")
    sistema.reservar_vuelo("McLovin", 500.0, "applepay")