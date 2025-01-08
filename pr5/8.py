import math

def calcular_factorial(n):
    """
    Calcula el factorial de un número entero no negativo.

    Parámetros:
    n (int): Número entero no negativo para calcular su factorial.

    Retorna:
    int: El factorial de `n`.

    Levanta:
    ValueError: Si `n` es un número negativo.
    """
    if n < 0:
        raise ValueError("El número debe ser un entero no negativo.")
    return math.factorial(n)


if __name__ == "__main__":
    while True:
        try:
            a = int(input("Introduzca un número entero no negativo: "))
            factorial = calcular_factorial(a)
            print(f"\nEl factorial de {a} es: {factorial}\n")
        except ValueError as e:
            print(f"Error: {e}. Por favor, intenta de nuevo.\n")
