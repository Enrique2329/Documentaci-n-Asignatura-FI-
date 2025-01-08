import math



def volumen_esfera(r):

    """

    Calcula el volumen de una esfera dado su radio.

    Args:
        r (float): El radio de la esfera.

    Returns:
        float: El volumen de la esfera calculado como (4/3) * π * r^3.
    """
    return (4/3) * math.pi * r**3

def main():
    """
    Solicita al usuario el radio de una esfera, calcula su volumen
    y muestra el resultado en pantalla.
    """
    # Solicitar al usuario el radio de la esfera
    radio = float(input("Introduce el radio de la esfera: "))
    
    # Calcular el volumen de la esfera
    volumen = volumen_esfera(radio)
    
    # Mostrar el resultado
    print(f"El volumen de la esfera de radio {radio} es: {volumen:.2f} cm³")

if __name__ == "__main__":
    main()
