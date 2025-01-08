def evaluar_beneficios(ingresos: int, gastos: int) -> int:
    """
    Calcula los beneficios de una empresa a partir de sus ingresos y gastos.

    Esta función evalúa si los beneficios de una empresa son positivos, negativos o nulos, 
    y devuelve un valor entero dependiendo de la situación de la empresa.

    - Si los beneficios son positivos, imprime "La empresa es solvente" y devuelve +1.
    - Si los beneficios son cero, imprime "Se ha alcanzado el punto de equilibrio" y devuelve 0.
    - Si los beneficios son negativos, imprime "La empresa esta en numeros rojos" y devuelve -1.

    Args:
        ingresos (int): Los ingresos de la empresa.
        gastos (int): Los gastos de la empresa.

    Returns:
        int: 
            +1 si la empresa es solvente (beneficios positivos).
            0 si se ha alcanzado el punto de equilibrio (beneficios cero).
            -1 si la empresa está en números rojos (beneficios negativos).
    """
    beneficios = ingresos - gastos

    if beneficios > 0:
        print("\nLa empresa es solvente")
        return +1

    elif beneficios == 0:
        print("\nSe ha alcanzado el punto de equilibrio")
        return 0

    elif beneficios < 0:
        print("La empresa esta en numeros rojos")
        return -1


if __name__ == "__main__":
    # Solicitar ingresos y gastos al usuario
    ingresos = int(input("Introduzca ingresos: "))
    gastos = int(input("Introduzca gastos: "))

    # Llamar a la función y mostrar el resultado
    resultado = evaluar_beneficios(ingresos, gastos)

    print(f"Resultado: {resultado}")
