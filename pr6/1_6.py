import numpy as np

def operaciones_matrices():
    """
    Función que realiza operaciones con dos matrices de 3x5:
    - Suma
    - Diferencia
    - Producto elemento a elemento
    
    Luego imprime los resultados de estas operaciones.
    """
    # Definición de las dos matrices de 3x5
    M = np.array([[1, 2, 3, 4, 5], 
                  [5, 6, 7, 8, 9],
                  [9, 2, 4, 1, 5]])

    N = np.array([[4, 3, 1, 5, 1],
                  [1, 6, 3, 6, 2],
                  [6, 8, 3, 8, 1]])
    
    # Suma de las matrices
    suma = M + N

    # Diferencia de las matrices
    resta = M - N

    # Producto elemento a elemento de las matrices
    producto = M * N

    # Imprimir los resultados
    print(f"\nLa matriz suma es:\n {suma}\n")
    print(f"La matriz diferencia es:\n {resta}\n")
    print(f"La matriz producto es:\n {producto}\n")

# Llamar a la función para ejecutar las operaciones
operaciones_matrices()
