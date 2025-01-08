def dia_de_la_semana(dia: int) -> str:
    """
    Dada una entrada numérica entre 1 y 7, devuelve el correspondiente día de la semana.

    La función recibe un número entero entre 1 y 7 e imprime el nombre del día de la semana correspondiente.

    Args:
        dia (int): Un número entero entre 1 y 7, donde:
                    1 = lunes, 2 = martes, ..., 7 = domingo.

    Returns:
        str: El nombre del día de la semana correspondiente al número proporcionado.

    Raises:
        ValueError: Si el número ingresado no está entre 1 y 7.
    """
    mylist = ["", "lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
    
    if 1 <= dia <= 7:
        return mylist[dia]
    else:
        raise ValueError("El número ingresado debe estar entre 1 y 7.")

if __name__ == "__main__":
    try:
        dia = int(input("Introduce el número del día de la semana (1 a 7): "))
        print(f"El día correspondiente es: {dia_de_la_semana(dia)}")
    except ValueError as e:
        print(e)
