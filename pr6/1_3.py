import numpy as np

def suma(vectorA, vectorB):
    """
    Suma dos vectores de 3 componentes.

    Argumentos:
    vectorA -- Primer vector (numpy array).
    vectorB -- Segundo vector (numpy array).

    Retorna:
    El vector resultado de la suma de vectorA y vectorB.
    """
    return np.add(vectorA, vectorB)

def resta(vectorA, vectorB):
    """
    Resta dos vectores de 3 componentes.

    Argumentos:
    vectorA -- Primer vector (numpy array).
    vectorB -- Segundo vector (numpy array).

    Retorna:
    El vector resultado de la resta de vectorA y vectorB.
    """
    return np.subtract(vectorA, vectorB)

def productoEscalar(vectorA, vectorB):
    """
    Calcula el producto escalar de dos vectores de 3 componentes.

    Argumentos:
    vectorA -- Primer vector (numpy array).
    vectorB -- Segundo vector (numpy array).

    Retorna:
    El resultado del producto escalar entre vectorA y vectorB.
    """
    return np.dot(vectorA, vectorB)

# Definimos los vectores
vectorA = np.array([1, 2, 3])
vectorB = np.array([2, 7, 5])

# Realizamos las operaciones
suma_resultado = suma(vectorA, vectorB)
resta_resultado = resta(vectorA, vectorB)
producto_resultado = productoEscalar(vectorA, vectorB)

# Imprimimos los resultados
print(f"\nEl resultado de la suma es: {suma_resultado}")
print(f"\nEl resultado de la resta es: {resta_resultado}")
print(f"\nEl resultado del producto escalar es: {producto_resultado}\n")
