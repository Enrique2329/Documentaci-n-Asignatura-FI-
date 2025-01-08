def dividir(dividendo, divisor):
    """
    Realiza la división de dos números, verificando que el divisor no sea cero.

    Esta función recibe dos números: el dividendo y el divisor, y devuelve el 
    resultado de la división. Si el divisor es cero, la función devuelve 
    un mensaje indicando que no es posible realizar la división.

    Args:
        dividendo (float): El número que será dividido.
        divisor (float): El número que divide al dividendo.

    Returns:
        float or str: El resultado de la división si el divisor es diferente de cero, 
                      o un mensaje de error si el divisor es cero.
    """
    if divisor == 0:
        return "La división no es posible, no se puede dividir entre 0"
    else:
        return dividendo / divisor


if __name__ == "__main__":
    # Solicitar el dividendo al usuario
    dividendo = float(input("Introduzca el dividendo: "))

    # Solicitar el divisor al usuario
    divisor = float(input("Introduzca el divisor: "))

    # Llamar a la función dividir y obtener el resultado
    resultado = dividir(dividendo, divisor)

    # Mostrar el resultado
    if isinstance(resultado, str):  # Si el resultado es un mensaje de error (str)
        print(resultado)
    else:
        print(f"\nEl resultado de la división es: {resultado:.2f}")
