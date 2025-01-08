def deteccion(a: int, b: int, c: int) -> bool:
    """
    Detecta si tres números se han introducido en orden creciente.

    La función evalúa si los tres números dados están en orden creciente, 
    es decir, si el primero es menor que el segundo y el segundo es menor que el tercero.

    Args:
        a (int): Primer número.
        b (int): Segundo número.
        c (int): Tercer número.

    Returns:
        bool: 
            True si los números están en orden creciente.
            False si no están en orden creciente.
    """
    if a < b < c:
        return True
    else:
        return False


if __name__ == "__main__":
    # Solicitar los tres números al usuario y convertirlos a enteros
    a = int(input("Introduzca el primer número: "))
    b = int(input("Introduzca el segundo número: "))
    c = int(input("Introduzca el tercer número: "))

    # Llamar a la función deteccion y mostrar el resultado
    resultado = deteccion(a, b, c)
    print(f"\n¿Los números están ordenados en orden creciente?: {resultado}")
