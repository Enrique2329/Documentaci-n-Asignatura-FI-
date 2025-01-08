def es_palindromo(cadena):
    """
    Esta función comprueba si una cadena es un palíndromo. Una palabra es un palíndromo si se lee 
    igual de izquierda a derecha que de derecha a izquierda.

    Parámetros:
    cadena (str): La cadena que se desea comprobar.

    Retorna:
    bool: Retorna True si la cadena es un palíndromo, False en caso contrario.

    Ejemplo:
    >>> es_palindromo("reconocer")
    True
    >>> es_palindromo("hola")
    False
    """
    # Eliminar espacios y convertir a minúsculas para una comparación más flexible
    cadena = cadena.replace(" ", "").lower()
    
    # Comprobar si la cadena es igual a su reverso
    return cadena == cadena[::-1]

# Solicitar la cadena al usuario
cadena_og = input("Introduce una cadena: ")

# Llamar a la función para verificar si es un palíndromo
if es_palindromo(cadena_og):
    print("Sí, es un palíndromo")
else:
    print("No, no es un palíndromo")
