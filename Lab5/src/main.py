from decorator import basicTarifa, studentDecorator, greenDecorator


def main():
    print("=== Simulación de sistema de transporte ===\n")

    # Tarifa base
    tarifa_base = basicTarifa(2450)
    print(f"Tarifa base total: {tarifa_base.calcular_tarifa()} colones\n")

    # Aplicar decoradores
    tarifa_estudiante = studentDecorator(tarifa_base)
    print("Aplicando descuento de estudiante (-15%)")

    tarifa_final = greenDecorator(tarifa_estudiante)
    print("Aplicando descuento verde (-5%)")

    # Resultado final (redondeando a entero como en ejemplo)
    print(f"Tarifa final total: {tarifa_final.calcular_tarifa():.0f} colones\n")


if __name__ == "__main__":
    main()
