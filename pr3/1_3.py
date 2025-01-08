def solucion_ecuacion_primero_grado(a, b):
    """
    Calcula la solución de una ecuación de primer grado de la forma ax + b = 0.

    Args:
        a (float): El coeficiente de la variable x.
        b (float): El término independiente.

    Returns:
        str: Una cadena que describe la solución:
            - Si `a != 0`, retorna el valor de x.
            - Si `a == 0` y `b == 0`, indica que la ecuación tiene infinitas soluciones.
            - Si `a == 0` y `b != 0`, indica que no hay solución.
    """
    if a != 0:
        # Calculamos el valor de x
        x = -b / a
        return f"El valor de x es: {x}"
    else:
        # Si 'a' es 0, evaluamos las condiciones de la ecuación
        if b == 0:
            return "La ecuación tiene infinitas soluciones."
        else:
            return "La ecuación no tiene solución."

def main():
    """
    Solicita al usuario los coeficientes de una ecuación de primer grado
    y muestra su solución.
    """
    # Solicitar al usuario los coeficientes
    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))
    
    # Obtener y mostrar la solución
    resultado = solucion_ecuacion_primero_grado(a, b)
    print(resultado)

if __name__ == "__main__":
    main()
