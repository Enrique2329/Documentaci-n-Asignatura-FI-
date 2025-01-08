def calcular_area_triangulo(base, altura):
    """
    Calcula el área de un triángulo dado su base y altura.

    Args:
        base (float): El valor de la base del triángulo.
        altura (float): El valor de la altura del triángulo.

    Returns:
        float: El área del triángulo calculada con la fórmula (base * altura) / 2.
    """
    # Calcular el área
    area = (base * altura) / 2
    return area


if __name__ == "__main__":
    # Solicitar los valores de la base y la altura del triángulo
    b = float(input("Introduce el valor de la base: "))
    h = float(input("Introduce el valor de la altura: "))

    # Calcular el área
    area_triangulo = calcular_area_triangulo(b, h)

    # Mostrar el resultado
    print(f"\nEl valor del área del triángulo es: {area_triangulo}")
