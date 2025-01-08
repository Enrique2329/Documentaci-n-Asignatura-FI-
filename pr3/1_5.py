def calcular_porcentaje(a, b):
    """
    Calcula el porcentaje de una parte con respecto a un total.

    Args:
        a (float): El valor de la parte.
        b (float): El valor del total.

    Returns:
        float: El porcentaje calculado de la parte con respecto al total.
        str: Un mensaje indicando si el cálculo fue posible o no.
    """
    if b != 0:
        # Calculamos el porcentaje
        porcentaje = (a / b) * 100
        return f"El valor es: {porcentaje:.2f} %"
    else:
        return "No es posible calcular el porcentaje, inserte otro valor total."

def main():
    """
    Solicita al usuario los valores de la parte y el total, y calcula el porcentaje.
    Si el total es cero, pide al usuario que ingrese un valor válido.
    """
    while True:
        try:
            # Solicitar al usuario los valores
            a = float(input("Ingrese el valor de la parte: "))
            b = float(input("Ingrese el valor del total: "))
            
            # Llamar a la función para calcular el porcentaje
            resultado = calcular_porcentaje(a, b)
            
            # Mostrar el resultado
            print(resultado)
            
            # Si el total es distinto de cero, termina el bucle
            if b != 0:
                break
                
        except ValueError:
            print("Por favor, ingresa valores numéricos válidos para la parte y el total.")

if __name__ == "__main__":
    main()

