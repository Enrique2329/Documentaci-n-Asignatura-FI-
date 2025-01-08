def tabla_multiplicar(numero):
    """
    Muestra la tabla de multiplicar de un número natural dado.

    Parámetros:
    numero (int): El número natural cuya tabla de multiplicar se va a mostrar.

    Si el número dado es negativo, se muestra un mensaje indicando que debe ser un número natural.
    De lo contrario, muestra la tabla de multiplicar del número proporcionado, desde 1 hasta 10.
    """
    if numero < 0:
        print("Por favor, introduce un número natural (entero positivo).")
        return

    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


if __name__ == "__main__":
    # Solicitar un número natural al usuario y mostrar su tabla de multiplicar
    try:
        numero = int(input("Introduce un número natural: "))
        tabla_multiplicar(numero)
    except ValueError:
        print("Por favor, introduce un número entero válido.")
