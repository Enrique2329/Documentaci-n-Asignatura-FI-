def contar_vocales_consonantes(palabra):
    """
    Esta función toma una palabra y cuenta el número de vocales y consonantes que contiene.

    Parámetros:
    palabra (str): La palabra sobre la cual se va a contar las vocales y consonantes.

    Retorna:
    tuple: Un tuple con dos valores:
        - El número de vocales en la palabra.
        - El número de consonantes en la palabra.
    
    Ejemplo:
    >>> contar_vocales_consonantes("Hola")
    (2, 2)
    """
    vocales = "aeiouáàäéèëíìïóòöúùü"
    consonantes = "bcdfghjklmnpqrstvwxyz"
    
    num_vocales = 0
    num_consonantes = 0
    
    # Recorrer la palabra y contar las vocales y consonantes
    for letra in palabra.lower():  # Convertir la palabra a minúsculas para hacer una comparación insensible a mayúsculas
        if letra in vocales:
            num_vocales += 1
        elif letra in consonantes:
            num_consonantes += 1
    
    return num_vocales, num_consonantes

# Ejemplo de uso de la función
palabra = "Hola"
vocales, consonantes = contar_vocales_consonantes(palabra)
print(f"Vocales: {vocales}\nConsonantes: {consonantes}")
