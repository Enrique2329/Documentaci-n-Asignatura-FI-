# Este programa calcula el cuadrado de un número real e identifica si el resultado es un entero

def es_entero(numero):
    """
    Verifica si un número es entero.

    Args:
        numero (float): El número que se va a verificar.

    Returns:
        bool: True si el número es entero, False si no lo es.
    """
    if type(numero) == int:
        return True
    else:
        return False


def calcular_cuadrado():
    """
    Solicita al usuario un número real, calcula su cuadrado y verifica si el resultado es un número entero.

    El programa calcula el cuadrado de un número real, luego verifica si el resultado es entero y
    muestra un mensaje indicando si es entero o no.
    """
    while True:
        # Solicitar un número real al usuario
        numero_real = float(input("Introduce un número real cualquiera: "))
        
        # Calcular el cuadrado del número real
        numero_cuadrado = numero_real ** 2

        # Verificar si el cuadrado es un número entero
        if es_entero(numero_cuadrado):
            print(f"El cuadrado del número {numero_real} es {numero_cuadrado} y es un número entero.")
        else:
            print(f"El cuadrado del número {numero_real} es {numero_cuadrado} y no es un número entero.")


# Ejecutar la función principal
if __name__ == "__main__":
    calcular_cuadrado()


