def quitar_espacios(cadena_car):
    """
    Esta función recibe una cadena de caracteres y elimina los espacios en blanco al principio y al final.

    Parámetros:
    cadena_car (str): La cadena de caracteres a la cual se le eliminarán los espacios en blanco.

    Retorna:
    str: La cadena corregida sin espacios en blanco al principio y al final.

    Ejemplo:
    >>> quitar_espacios("   hola como estas   ")
    'hola como estas'
    """
    # Utilizamos la función strip() que elimina los espacios en blanco al principio y al final de la cadena
    cadena_corregida = cadena_car.strip()
    return cadena_corregida

# Solicitar la cadena de entrada
cadena_car = str(input("Introduce la cadena de caracteres deseada: "))

# Llamar a la función para corregir la cadena
cadena_corregida = quitar_espacios(cadena_car)

# Imprimir el resultado
print(f"La cadena corregida es: {cadena_corregida}")
