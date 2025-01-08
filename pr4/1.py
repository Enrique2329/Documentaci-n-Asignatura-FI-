def calcular_perimetro_area_cuadrado(lado):
    """
    Calcula el perímetro y el área de un cuadrado dado el valor de su lado.

    Args:
        lado (float): El valor del lado del cuadrado.

    Returns:
        tuple: Un tuple que contiene dos valores:
            - El perímetro del cuadrado (float).
            - El área del cuadrado (float).
    """
    # Calcular el perímetro
    perimetro = lado * 4

    # Calcular el área
    area = lado ** 2

    return perimetro, area


if __name__ == "__main__":
    # Solicitar el valor del lado del cuadrado
    lado = float(input("Introduce el lado del cuadrado: "))

    # Calcular el perímetro y el área
    perimetro, area = calcular_perimetro_area_cuadrado(lado)

    # Mostrar los resultados
    print(f"El perímetro del cuadrado es: {perimetro:.2f}")
    print(f"El área del cuadrado es: {area:.2f}")
