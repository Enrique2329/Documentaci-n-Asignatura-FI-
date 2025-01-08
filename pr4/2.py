def calcular_perimetro_area_rectangulo(lado1, lado2):
    """
    Calcula el perímetro y el área de un rectángulo dado el valor de sus dos lados.

    Args:
        lado1 (float): El valor del primer lado del rectángulo.
        lado2 (float): El valor del segundo lado del rectángulo.

    Returns:
        tuple: Un tuple que contiene dos valores:
            - El perímetro del rectángulo (float).
            - El área del rectángulo (float).
    """
    # Calcular el perímetro
    perimetro = 2 * (lado1 + lado2)

    # Calcular el área
    area = lado1 * lado2

    return perimetro, area


if __name__ == "__main__":
    # Solicitar los valores de los dos lados del rectángulo
    a = float(input("Introduce el primer lado: "))
    b = float(input("Introduce el segundo lado: "))

    # Calcular el perímetro y el área
    perimetro, area = calcular_perimetro_area_rectangulo(a, b)

    # Mostrar los resultados
    print(f"\nEl valor del perímetro es: {perimetro}\n")
    print(f"El valor del área es: {area}\n")
