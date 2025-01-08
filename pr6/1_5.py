import numpy as np

def llenar_y_sumar_matriz():
    """
    Función que llena una matriz de 3x3 con valores aleatorios entre 0 y 20,
    imprime la matriz, y luego imprime la suma de las filas y las columnas.
    """
    # Generar una matriz de 3x3 con valores aleatorios entre 0 y 20
    M = np.random.randint(0, 20, (3, 3))
    
    # Imprimir la matriz
    print(f"La matriz es:\n{M}")
    
    # Calcular la suma de las filas (axis=1)
    suma_filas = np.sum(M, axis=1)
    
    # Calcular la suma de las columnas (axis=0)
    suma_columnas = np.sum(M, axis=0)
    
    # Imprimir las sumas de las filas y las columnas
    print(f"\nLa suma de las filas es: {suma_filas}")
    print(f"La suma de las columnas es: {suma_columnas}")

# Llamar a la función para ejecutar el proceso
llenar_y_sumar_matriz()
