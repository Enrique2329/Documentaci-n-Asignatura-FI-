def desglosar_segundos(segundos_totales):
    """
    Desglosa una cantidad de segundos en su equivalente en horas, minutos y segundos.

    La función toma una cantidad total de segundos y devuelve su equivalente en
    horas, minutos y segundos utilizando división entera y el operador módulo.

    Args:
        segundos_totales (int): La cantidad de segundos a desglosar.

    Returns:
        tuple: Una tupla con las horas, minutos y segundos correspondientes.
    """
    horas = segundos_totales // 3600
    minutos = (segundos_totales % 3600) // 60
    segundos = segundos_totales % 60

    return horas, minutos, segundos


if __name__ == "__main__":
    # Solicitar la cantidad total de segundos
    segundos_totales = int(input("Introduce los segundos totales: "))

    # Llamar a la función para desglosar los segundos
    horas, minutos, segundos = desglosar_segundos(segundos_totales)

    # Mostrar el resultado
    print(f"\nLa conversión es: {horas} horas, {minutos} minutos y {segundos} segundos")



