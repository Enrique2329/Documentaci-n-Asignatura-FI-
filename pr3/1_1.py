'Calcular el area de un circulo de radio r'

import math

def area_circulo(r):
    """
    Calcula el área de un círculo dado su radio.

    Args:
        r (float): El radio del círculo.

    Returns:
        float: El área del círculo calculada como π * r^2.
    """
    return math.pi * r**2

def main():
    """
    Solicita al usuario el radio de un círculo, calcula el área
    y muestra el resultado en pantalla.
    """
    # Solicitar al usuario el radio
    radio = float(input("Introduce el radio del círculo: "))
    
    # Calcular el área del círculo
    area = area_circulo(radio)
    
    # Mostrar el resultado
    print(f"El área del círculo de radio {radio} es: {area:.2f} cm2")

if __name__ == "__main__":
    main()
