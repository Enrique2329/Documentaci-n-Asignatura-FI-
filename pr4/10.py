def convertir_a_pesetas(euros):
    """
    Convierte una cantidad en euros a pesetas.

    Esta función toma una cantidad en euros y la convierte a pesetas utilizando
    el tipo de cambio fijo de 1 euro = 166386 pesetas.

    Args:
        euros (float): La cantidad en euros a convertir.

    Returns:
        float: La cantidad equivalente en pesetas.
    """
    pesetas = 166386 * euros
    return pesetas


if __name__ == "__main__":
    while True:
        try:
            # Solicitar la cantidad en euros
            euros = float(input("Introduce la cantidad en euros a convertir (o '0' para salir): "))

            # Si el usuario ingresa 0, se sale del bucle
            if euros == 0:
                print("Saliendo del programa...")
                break

            # Llamar a la función para convertir euros a pesetas
            pesetas = convertir_a_pesetas(euros)

            # Mostrar el resultado
            print(f"\nLa equivalencia en pesetas son: {pesetas:.2f}")

        except ValueError:
            print("Por favor, introduce un número válido.")
