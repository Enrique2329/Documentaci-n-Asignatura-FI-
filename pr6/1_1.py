import numpy as np

def concatenar_vectores(N, M):
    """
    Dada dos vectores de enteros, de tamaños N y M respectivamente, esta función concatena ambos vectores
    en un nuevo vector que tiene un tamaño de N+M.
    
    Argumentos:
    N -- Primer vector de enteros (array de numpy o lista de Python).
    M -- Segundo vector de enteros (array de numpy o lista de Python).
    
    Retorna:
    Un nuevo vector que es la concatenación de N y M.
    """
    # Concatenar los dos vectores usando np.concatenate
    return np.concatenate([N, M])

# Ejemplo de uso
if __name__ == "__main__":
    # Definimos los vectores de ejemplo
    N = np.array([5, 1, 3, 15, 4])
    M = np.array([3, 4, 2])

    # Llamamos a la función para concatenar los vectores
    resultado = concatenar_vectores(N, M)

    # Mostramos el resultado de la concatenación
    print(f"El vector concatenado es: {resultado}")
