import math

def calcular_area_perimetro_triangulo(lado1, lado2, lado3):
    """
    Calcula el área y el perímetro de un triángulo dado sus tres lados utilizando la fórmula de Herón para el área.

    Args:
        lado1 (float): El valor del primer lado del triángulo.
        lado2 (float): El valor del segundo lado del triángulo.
        lado3 (float): El valor del tercer lado del triángulo.

    Returns:
        tuple: Un tuple que contiene dos valores:
            - El perímetro del triángulo (float).
            - El área del triángulo (float).
    """
    # Calcular el semiperímetro (s)
    s = (lado1 + lado2 + lado3) / 2

    # Calcular el área usando la fórmula de Herón
    area = math.sqrt(s * (s - lado1) * (s - lado2) * (s - lado3))

    # Calcular el perímetro
    perimetro = lado1 + lado2 + lado3

    return perimetro, area


if __name__ == "__main__":
    # Solicitar los valores de los tres lados del triángulo
    a = float(input("Introduce el lado a: "))
    b = float(input("Introduce el lado b: "))
    c = float(input("Introduce el lado c: "))

    # Calcular el área y el perímetro
    perimetro, area = calcular_area_perimetro_triangulo(a, b, c)

    # Mostrar los resultados
    print(f"\nEl perímetro del triángulo es: {perimetro:.2f}")
    print(f"El área del triángulo es: {area:.2f}")


        
