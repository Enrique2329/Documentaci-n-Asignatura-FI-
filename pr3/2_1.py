import math

# 1) Determinar si un número es primo
def es_primo(num):
    """
    Determina si un número es primo.

    Un número primo es aquel que solo es divisible por 1 y por sí mismo.

    Args:
        num (int): El número a verificar.

    Returns:
        bool: True si el número es primo, False si no lo es.
    """
    es_primo = True
    for i in range(2, int(num ** 0.5) + 1):  # Recorremos los posibles divisores hasta la raíz cuadrada del número
        if num % i == 0:
            es_primo = False  # Si encontramos un divisor, el número no es primo
            break
    return es_primo

# 2) Convertir grados Celsius a Kelvin
def celsius_a_kelvin(celsius):
    """
    Convierte grados Celsius a Kelvin.

    La fórmula para la conversión es: K = °C + 273

    Args:
        celsius (float): La temperatura en grados Celsius.

    Returns:
        float: La temperatura equivalente en grados Kelvin.
    """
    return celsius + 273

# 3) Encontrar el número mayor y menor de una lista
def analizar_lista_numeros(numeros):
    """
    Analiza una lista de números y devuelve el número mayor y menor de la lista.

    Args:
        numeros (list): Una lista de números enteros.

    Returns:
        tuple: El número mayor y menor de la lista.
    """
    return max(numeros), min(numeros)

def main():
    """
    Función principal que solicita al usuario una serie de entradas y realiza las tareas:
    1. Verifica si un número es primo.
    2. Convierte una temperatura de grados Celsius a Kelvin.
    3. Encuentra el número mayor y menor en una lista de números.
    """
    # 1) Solicitar un número y verificar si es primo
    while True:
        num = int(input("Introduce un número entero: "))  # Solicitar el número al usuario
        if es_primo(num):
            print(f"{num} es primo")
        else:
            print(f"{num} no es primo")
        break  # Salir del bucle tras un resultado

    # 2) Convertir grados Celsius a Kelvin
    grados_celsius = float(input("Introduce los grados Celsius: "))  # Solicitar grados Celsius
    grados_kelvin = celsius_a_kelvin(grados_celsius)
    print(f"Los grados Kelvin correspondientes son: {grados_kelvin}")

    # 3) Analizar lista de números
    numeros = list(map(int, input("Introduce una lista de números separados por espacios: ").split()))  # Crear la lista de números
    mayor, menor = analizar_lista_numeros(numeros)
    print(f"El número mayor es {mayor} y el menor es {menor}")

if __name__ == "__main__":
    main()
