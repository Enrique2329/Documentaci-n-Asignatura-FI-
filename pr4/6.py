def calcular_area_trapecio(base_mayor, base_menor, altura):
    """
    Calcula el área de un trapecio dado su base mayor, base menor y altura.

    La fórmula utilizada es:
        Área = ((base mayor + base menor) * altura) / 2

    Args:
        base_mayor (float): La longitud de la base mayor del trapecio.
        base_menor (float): La longitud de la base menor del trapecio.
        altura (float): La altura del trapecio.

    Returns:
        float: El área del trapecio.
    """
    # Calcular el área utilizando la fórmula del trapecio
    area = ((base_mayor + base_menor) * altura) / 2
    return area


if __name__ == "__main__":
    # Solicitar los valores de las bases y la altura del trapecio
    b_mayor = float(input("Introduce la base mayor: "))
    b_menor = float(input("Introduce la base menor: "))
    altura = float(input("Introduce la altura: "))

    # Calcular el área del trapecio
    area = calcular_area_trapecio(b_mayor, b_menor, altura)

    # Mostrar el resultado
    print(f"\nEl área del trapecio es: {area:.2f}")

