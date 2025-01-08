def calcular_producto_digitos(numero: int) -> int:
    """
    Calcula el producto de los dígitos de un número entero.

    Dado un número entero, la función calcula el producto de todos sus dígitos. 
    Por ejemplo, con el número 123, el producto sería 1 * 2 * 3 = 6.

    Parámetros:
    numero (int): El número entero cuyo producto de dígitos se va a calcular.

    Retorna:
    int: El producto de los dígitos del número.
    """
    # Asegurarse de trabajar con el valor absoluto del número
    numero = abs(numero)
    
    # Inicializar el producto como 1
    producto = 1

    # Iterar sobre los dígitos del número (como cadena de caracteres)
    for digito in str(numero):
        producto *= int(digito)  # Multiplicar el producto por el valor del dígito

    return producto


def obtener_numero() -> int:
    """
    Solicita un número entero al usuario una vez.

    Retorna:
    int: El número entero ingresado por el usuario.
    """
    try:
        numero = int(input("Ingrese un número entero: "))
        return numero
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
        return None


if __name__ == "__main__":
    # Ejecución del programa
    numero = obtener_numero()
    if numero is not None:
        producto_digitos = calcular_producto_digitos(numero)
        print(f"El producto de los dígitos del número {numero} es: {producto_digitos}")
