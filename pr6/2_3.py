def eliminar_a(cadena):
    """
    Esta función elimina todas las ocurrencias del caracter 'a' en una cadena de caracteres.

    Parámetros:
    cadena (str): La cadena de caracteres de la cual se eliminarán todas las 'a'.

    Retorna:
    str: La cadena sin las ocurrencias del caracter 'a'.

    Ejemplo:
    >>> eliminar_a("banana")
    'bn'
    """
    # Creamos una cadena auxiliar para almacenar los caracteres que no sean 'a'
    cadena_auxiliar = ""
    
    # Iteramos sobre cada carácter en la cadena
    for caracter in cadena:
        # Si el carácter no es 'a', lo agregamos a la cadena auxiliar
        if caracter != 'a':
            cadena_auxiliar += caracter
    
    return cadena_auxiliar

# Solicitar la cadena de entrada
cadena = input("Introduce la cadena deseada: ")

# Llamar a la función para eliminar las 'a'
cadena_sin_a = eliminar_a(cadena)

# Imprimir el resultado
print(f"Cadena original: {cadena}")
print(f"Cadena sin 'a': {cadena_sin_a}")
