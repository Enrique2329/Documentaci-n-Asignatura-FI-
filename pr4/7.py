def intercambiar_valores(a, b):
    """
    Intercambia los valores de dos variables.

    La función toma dos números, intercambia sus valores y los devuelve.

    Args:
        a (float): El primer número.
        b (float): El segundo número.

    Returns:
        tuple: Una tupla con los valores de 'b' y 'a' intercambiados.
    """
    # Intercambiar los valores
    a, b = b, a
    return a, b


if __name__ == "__main__":
    # Solicitar los valores de A y B
    a = float(input("Introduzca A: "))
    b = float(input("Introduzca B: "))

    # Llamar a la función para intercambiar los valores
    a, b = intercambiar_valores(a, b)

    # Mostrar los valores intercambiados
    print(f"El valor de 'a' intercambiado es: {a}")
    print(f"El valor de 'b' intercambiado es: {b}")
