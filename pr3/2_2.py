# 1) Convertir un número entero a cadena y viceversa
def convertir_numero():
    """
    Convierte un número entero a cadena y viceversa, mostrando los tipos de datos en cada paso.

    Solicita al usuario un número entero, lo convierte a cadena, lo muestra con su tipo, 
    y luego lo convierte nuevamente a entero y muestra el tipo de nuevo.
    """
    # Solicitar un número entero al usuario
    numero = int(input("Introduce un número entero: "))

    # Convertir a cadena y mostrar el tipo
    numero_str = str(numero)
    print(f"El número como cadena es '{numero_str}', y su tipo es {type(numero_str)}")

    # Convertir de nuevo a entero y mostrar el tipo
    numero_int = int(numero_str)
    print(f"El número como entero es {numero_int}, y su tipo es {type(numero_int)}")

# 2) Convertir un número decimal como cadena a flotante y calcular su cuadrado
def convertir_y_calcular_cuadrado():
    """
    Convierte un número decimal representado como cadena a tipo flotante, 
    luego calcula y muestra el cuadrado de ese número.

    Solicita al usuario un número decimal como cadena, lo convierte a flotante y calcula su cuadrado.
    """
    # Solicitar un número decimal como cadena
    numero_cadena = input("Introduce un número decimal (por ejemplo, 3.14): ")

    # Convertir la cadena a flotante
    numero_float = float(numero_cadena)
    print(f"El número como flotante es {numero_float}, y su tipo es {type(numero_float)}")

    # Calcular el cuadrado del número
    cuadrado = numero_float ** 2
    print(f"El cuadrado de {numero_float} es {cuadrado}")

# 3) Convertir una lista de palabras a un conjunto para eliminar duplicados y luego volver a una lista
def eliminar_duplicados():
    """
    Convierte una lista de palabras a un conjunto para eliminar duplicados, 
    y luego vuelve a convertir el conjunto en una lista.

    Solicita al usuario una lista de palabras separadas por espacios, elimina los duplicados 
    convirtiéndola en un conjunto, y luego vuelve a convertir el conjunto a una lista.
    """
    # Solicitar una lista de palabras al usuario
    palabras = input("Introduce una lista de palabras separadas por espacios: ").split()

    # Convertir la lista a un conjunto para eliminar duplicados
    palabras_unicas = set(palabras)
    print(f"Palabras únicas (como conjunto): {palabras_unicas}")

    # Convertir el conjunto de nuevo a una lista
    palabras_unicas_lista = list(palabras_unicas)
    print(f"Palabras únicas (como lista): {palabras_unicas_lista}")

def main():
    """
    Función principal que ejecuta las tres tareas de conversión de tipos de datos:
    1. Convierte un número entero a cadena y viceversa.
    2. Convierte un número decimal en cadena a flotante y calcula su cuadrado.
    3. Elimina duplicados de una lista de palabras usando un conjunto y luego la convierte de nuevo a lista.
    """
    # Ejecutar las tres funciones de conversión
    convertir_numero()
    convertir_y_calcular_cuadrado()
    eliminar_duplicados()

if __name__ == "__main__":
    main()



