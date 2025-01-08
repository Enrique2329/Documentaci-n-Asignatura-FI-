def es_numero_perfecto(n):
    """
    Determina si un número entero dado es perfecto.

    Un número perfecto es aquel que es igual a la suma de sus divisores propios 
    (excluyendo el mismo número). Por ejemplo, el número 6 es perfecto porque 
    sus divisores son 1, 2 y 3, y 1 + 2 + 3 = 6.

    Parámetros:
    n (int): El número a verificar.

    Retorna:
    bool: True si el número es perfecto, False si no lo es.
    """
    if n <= 0:
        print("Los números deben ser enteros positivos.")
        return False
    
    suma_divisores = sum(i for i in range(1, n) if n % i == 0)
    return suma_divisores == n


if __name__ == "__main__":
    # Solicitar al usuario que ingrese un número entero
    numero = int(input("Introduce un número entero: "))

    # Verificar si el número ingresado es perfecto
    if es_numero_perfecto(numero):
        print(f"{numero} es un número perfecto.")
    else:
        print(f"{numero} no es un número perfecto.")
