import numpy as np

def visualizar_hasta_valor(vector, A):
    """
    Dado un vector de enteros de tamaño N, esta función visualiza los valores de los elementos
    hasta encontrar el primer elemento cuyo valor sea mayor o igual a un número A inclusive.
    El resto de los elementos no se visualizarán.
    
    Argumentos:
    vector -- El vector de enteros (array de numpy).
    A -- El número límite para visualizar los elementos.
    """
    for elemento in vector:
        print(elemento)
        if elemento >= A:
            break

# Ejemplo de uso
if __name__ == "__main__":
    # Definimos el vector y el valor A
    vector = np.array([1, 3, 5, 7, 9, 2, 4, 6])
    A = 5

    # Llamamos a la función para visualizar los elementos
    visualizar_hasta_valor(vector, A)
