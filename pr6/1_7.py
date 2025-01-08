import numpy as np
from numpy.linalg import det, inv

def resolver_sistema_ecuaciones():
    """
    Resuelve un sistema de tres ecuaciones lineales con tres incógnitas utilizando matrices.
    
    El sistema de ecuaciones se representa como:
    A * X = B
    donde:
        A es la matriz de coeficientes 3x3,
        X es el vector de incógnitas 3x1,
        B es el vector de términos independientes 3x1.

    El programa realiza los siguientes pasos:
    1. Solicita al usuario ingresar los valores de la matriz de coeficientes (A) y del vector de términos independientes (B).
    2. Calcula el determinante de la matriz de coeficientes A.
    3. Si el determinante de A es cero, informa que el sistema no tiene solución única.
    4. Si el determinante no es cero, calcula la matriz inversa de A.
    5. Resuelve el sistema de ecuaciones utilizando la fórmula X = A⁻¹ * B.
    6. Muestra la solución del sistema, es decir, el vector de incógnitas X.
    
    Ejemplo de uso:
    El usuario debe ingresar las entradas de la matriz A y el vector B de la siguiente manera:
    - Una matriz A de 3x3 con los coeficientes de las ecuaciones.
    - Un vector B de 3x1 con los términos independientes.

    El programa luego calcula y muestra el determinante de A, la matriz inversa de A (si es posible), y la solución del sistema de ecuaciones.
    
    Requisitos:
    - El sistema debe tener una solución única, lo que implica que el determinante de la matriz A debe ser diferente de cero.

    Retorna:
    None: La función imprime la solución en consola.
    """
    
    # Solicitar las dimensiones de la matriz de ecuaciones
    print("Introduce los valores de la matriz del sistema de ecuaciones (3x3):")
    matriz_ecuaciones = np.zeros((3, 3))  # Definimos una matriz 3x3 para el sistema de ecuaciones
    for i in range(3):
        for j in range(3):
            matriz_ecuaciones[i, j] = float(input(f"Valor en la posición ({i+1}, {j+1}) de la matriz A: "))
    
    # Solicitar el vector de términos independientes
    print("\nIntroduce los valores del vector de términos independientes (3x1):")
    matriz_soluciones = np.zeros((3, 1))  # Definimos una matriz columna 3x1 para los términos independientes
    for i in range(3):
        matriz_soluciones[i, 0] = float(input(f"Valor en la posición ({i+1}) de la matriz B: "))
    
    # Mostrar la matriz de ecuaciones (A) y el vector de soluciones (B)
    print("\nMatriz del sistema (A):")
    print(matriz_ecuaciones)
    
    print("\nVector de términos independientes (B):")
    print(matriz_soluciones)

    # Calcular y mostrar el determinante de la matriz de coeficientes
    determinante = det(matriz_ecuaciones)
    print(f"\nEl determinante de la matriz A es: {determinante}")
    
    if determinante == 0:
        print("El sistema no tiene solución única, ya que el determinante es cero.")
        return
    
    # Calcular y mostrar la matriz inversa
    inversa = inv(matriz_ecuaciones)
    print(f"\nLa matriz inversa de A es:")
    print(inversa)

    # Resolver el sistema de ecuaciones utilizando la matriz inversa
    soluciones = np.dot(inversa, matriz_soluciones)
    
    # Mostrar la solución
    print("\nLa solución del sistema de ecuaciones es:")
    print(soluciones)

# Solo ejecuta la función si este script es ejecutado directamente
if __name__ == "__main__":
    resolver_sistema_ecuaciones()
