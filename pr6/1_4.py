import numpy as np

def maximo(vector):
    """
    Devuelve el valor máximo de un vector de números reales.

    Argumento:
    vector -- Un array de números reales.

    Retorna:
    El valor máximo del vector.
    """
    return np.max(vector)

def minimo(vector):
    """
    Devuelve el valor mínimo de un vector de números reales.

    Argumento:
    vector -- Un array de números reales.

    Retorna:
    El valor mínimo del vector.
    """
    return np.min(vector)

def media(vector):
    """
    Devuelve la media de los valores de un vector de números reales.

    Argumento:
    vector -- Un array de números reales.

    Retorna:
    La media de los valores del vector.
    """
    return np.mean(vector)

def ejecutar_calculos():
    """
    Solicita al usuario un vector de números reales y calcula el valor máximo, mínimo y la media del vector.

    El usuario ingresa un número entero N, que representa la cantidad de elementos del vector, 
    seguido de los valores reales que conforman dicho vector. Luego se calculan y muestran:
    - El valor máximo del vector.
    - El valor mínimo del vector.
    - La media de los valores del vector.
    
    No retorna ningún valor, solo imprime los resultados en consola.
    """
    # Leer el entero N
    N = int(input("Ingrese el número de elementos en el vector: "))

    # Leer el vector de N reales
    vector = np.array([float(input(f"Ingrese el valor real {i+1}: ")) for i in range(N)])

    # Calcular y mostrar el máximo, mínimo y media usando las funciones
    max_value = maximo(vector)
    min_value = minimo(vector)
    mean_value = media(vector)

    # Imprimir los resultados
    print(f"El valor máximo del vector es: {max_value}")
    print(f"El valor mínimo del vector es: {min_value}")
    print(f"La media de los valores del vector es: {mean_value:.2f}")

# Solo ejecuta la función si este script es ejecutado directamente
if __name__ == "__main__":
    ejecutar_calculos()
