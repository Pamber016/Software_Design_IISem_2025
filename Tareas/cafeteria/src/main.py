from modelo.SistemaPedidos import SistemaPedidos
from observer.Cliente import Cliente
from productos import (
    Cafe, TeVerde, Espresso,
    Croissant, TostadaFrancesa, Brownie,
    Leche, Crema, Canela, 
    RellenoChocolate, RellenoCrema, ToppingChocolate, ToppingMani
)

def main():
    print("=== Simulación de cafetería ===\n")
    
    # Crear sistema
    sistema = SistemaPedidos()
    
    # Crear clientes
    ana = Cliente("Ana")
    carlos = Cliente("Carlos")
    amber = Cliente("Amber")
    
    # Pedido de Ana
    cafe_ana = Leche(Canela(Cafe()))
    croissant_ana = RellenoChocolate(Croissant())
    
    sistema.agregar_pedido(cafe_ana, ana)
    sistema.agregar_pedido(croissant_ana, ana)

    print("\n") # Separador de pedidos
    
    # Pedido de Carlos
    te_carlos = TeVerde()
    cafe_carlos = Crema(Espresso())
    croissant_carlos = ToppingChocolate(RellenoCrema(Croissant()))
    
    sistema.agregar_pedido(te_carlos, carlos)
    sistema.agregar_pedido(cafe_carlos, carlos)
    sistema.agregar_pedido(croissant_carlos, carlos)

    print("\n") # Separador de pedidos

    # Pedido de Amber
    brownie_amber = ToppingMani(Brownie())
    tostada_amber = TostadaFrancesa()

    sistema.agregar_pedido(brownie_amber, amber)
    sistema.agregar_pedido(tostada_amber, amber)
    
    # Procesar todos los pedidos
    sistema.procesar_pedidos()

if __name__ == "__main__":
    main()