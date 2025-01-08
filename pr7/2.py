# 1. Función que devuelve la suma y el producto de los elementos de la tupla
def suma_y_producto(tupla):
    """
    Devuelve la suma y el producto de los elementos de la tupla.
    
    Parámetros:
    tupla (tuple): Tupla de números enteros.
    
    Retorna:
    tuple: Una tupla con la suma y el producto de los elementos.
    """
    suma = sum(tupla)
    producto = 1
    for num in tupla:
        producto *= num
    return (suma, producto)

# 2. Función que devuelve el mínimo y el máximo de los elementos de la tupla
def min_y_max(tupla):
    """
    Devuelve el mínimo y el máximo de los elementos de la tupla.
    
    Parámetros:
    tupla (tuple): Tupla de números enteros.
    
    Retorna:
    tuple: Una tupla con el mínimo y el máximo de los elementos.
    """
    minimo = min(tupla)
    maximo = max(tupla)
    return (minimo, maximo)

# 3. Función que devuelve la tupla invertida y su longitud
def invertir_y_longitud(tupla):
    """
    Devuelve una tupla invertida y su longitud.
    
    Parámetros:
    tupla (tuple): Tupla de números.
    
    Retorna:
    tuple: Una tupla con la versión invertida y la longitud de la tupla original.
    """
    invertida = tupla[::-1]
    longitud = len(tupla)
    return (invertida, longitud)

# 4. Función que devuelve una tupla con los elementos pares e impares separados
def pares_e_impares(tupla):
    """
    Devuelve una tupla con los elementos pares e impares separados.
    
    Parámetros:
    tupla (tuple): Tupla de números enteros.
    
    Retorna:
    tuple: Una tupla con dos sub-tuplas: una con los números pares y otra con los números impares.
    """
    pares = tuple(x for x in tupla if x % 2 == 0)
    impares = tuple(x for x in tupla if x % 2 != 0)
    return (pares, impares)

# 5. Función que devuelve una tupla con los elementos elevados al cuadrado y al cubo
def cuadrados_y_cubos(tupla):
    """
    Devuelve una tupla con los elementos elevados al cuadrado y al cubo.
    
    Parámetros:
    tupla (tuple): Tupla de números enteros.
    
    Retorna:
    tuple: Una tupla con dos sub-tuplas: una con los cuadrados y otra con los cubos de los elementos.
    """
    cuadrados = tuple(x**2 for x in tupla)
    cubos = tuple(x**3 for x in tupla)
    return (cuadrados, cubos)


# Funciones de ejemplo para elegir
def ejecutar_funcion_elegida(opcion, tupla):
    """
    Ejecuta la función elegida por el usuario, proporcionando resultados basados en la opción seleccionada.
    
    Parámetros:
    opcion (int): Número que representa la función que el usuario quiere ejecutar.
    tupla (tuple): Tupla de números que se utilizará como parámetro para la función seleccionada.
    
    Retorna:
    None
    """
    if opcion == 1:
        print(suma_y_producto(tupla))
    elif opcion == 2:
        print(min_y_max(tupla))
    elif opcion == 3:
        print(invertir_y_longitud(tupla))
    elif opcion == 4:
        print(pares_e_impares(tupla))
    elif opcion == 5:
        print(cuadrados_y_cubos(tupla))
    else:
        print("Opción no válida. Elige un número entre 1 y 5.")


# Ejemplo de uso
mi_tupla = (1, 2, 3, 4)

# Llama a la función deseada, elige el número de la función que quieres ejecutar
# Ejecuta por ejemplo la opción 1 (suma y producto):
ejecutar_funcion_elegida(1, mi_tupla)

# Puedes cambiar el número de la opción para ejecutar diferentes funciones
# Ejecuta por ejemplo la opción 4 (pares e impares):
# ejecutar_funcion_elegida(4, mi_tupla)
