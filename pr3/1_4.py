import math

def resolver_ecuacion_segundo_grado(a, b, c):
    """
    Resuelve una ecuación de segundo grado de la forma ax^2 + bx + c = 0.

    Args:
        a (float): El coeficiente de x^2.
        b (float): El coeficiente de x.
        c (float): El término independiente.

    Returns:
        str: Mensaje indicando las soluciones de la ecuación:
            - Si el discriminante es positivo, retorna las dos soluciones reales.
            - Si el discriminante es cero, retorna una solución real.
            - Si el discriminante es negativo, indica que no tiene soluciones reales.
    """
    discriminante = b**2 - (4 * a * c)
    
    if discriminante > 0:
        # Si el discriminante es positivo, hay dos soluciones reales.
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return f"Las soluciones son: x1 = {x1:.2f} y x2 = {x2:.2f}"
    
    elif discriminante == 0:
        # Si el discriminante es cero, hay una solución real.
        x = -b / (2 * a)
        return f"La solución única es: x = {x:.2f}"
    
    else:
        # Si el discriminante es negativo, no tiene soluciones reales.
        return "La ecuación no tiene soluciones reales."

def main():
    """
    Solicita al usuario los coeficientes de una ecuación de segundo grado
    y muestra las soluciones de la ecuación.
    """
    while True:
        try:
            # Solicitar al usuario los coeficientes
            a = float(input("Ingrese el valor de a (coeficiente de x^2): "))
            b = float(input("Ingrese el valor de b (coeficiente de x): "))
            c = float(input("Ingrese el valor de c (término independiente): "))
            
            # Verificar que 'a' no sea cero (no es una ecuación cuadrática)
            if a == 0:
                print("El valor de 'a' no puede ser cero en una ecuación cuadrática.")
                continue
            
            # Resolver la ecuación y mostrar las soluciones
            resultado = resolver_ecuacion_segundo_grado(a, b, c)
            print(resultado)
            break  # Salir del bucle después de calcular la solución

        except ValueError:
            print("Por favor ingresa números válidos para los coeficientes.")

if __name__ == "__main__":
    main()
