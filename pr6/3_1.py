def lista_metodos():
    """
    Esta función demuestra la utilidad de varios métodos de listas en Python.
    
    1. Ordena una lista de menor a mayor utilizando el método sort().
    2. Ordena la misma lista de mayor a menor utilizando sort(reverse=True).
    3. Elimina el último elemento de la lista utilizando el método pop().
    4. Muestra la posición de un elemento en una lista utilizando index().
    5. Añade un nuevo elemento a la lista utilizando append().
    6. Elimina un elemento específico de la lista utilizando remove().
    
    Ejemplo:
    >>> lista_metodos()
    """
    # Definimos una lista de enteros
    l = [3, 1, 2]
    print(f"Lista original: {l}")
    
    # Ordenar la lista de menor a mayor
    l.sort()
    print(f"En orden de menor a mayor: {l}") 

    # Ordenar la lista de mayor a menor
    l.sort(reverse=True)
    print(f"En orden de mayor a menor: {l}") 

    # Eliminar el último elemento de la lista
    l.pop()
    print(f"Eliminamos el último valor de la lista: {l}")

    # Lista de nombres
    a = ["Antonio", "Miguel", "Manolo"]
    
    # Obtener la posición de un elemento en la lista
    print(f"La posición de Manolo en la lista es: {a.index('Manolo')}")

    # Añadir un nuevo elemento a la lista
    a.append("Juan")
    print(f"Lista después de añadir a Juan: {a}")

    # Eliminar un elemento específico de la lista
    a.remove("Miguel")
    print(f"Lista después de eliminar a Miguel: {a}")

# Llamamos a la función
lista_metodos()
