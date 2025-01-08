def verificar_condiciones_logicas():
    """
    Realiza dos verificaciones lógicas utilizando operadores 'and' y 'or'.

    Primero, evalúa si ambas condiciones son verdaderas usando el operador 'and':
    - Si 'a' es mayor que 2 y 'b' es menor que 15.
    
    Luego, evalúa si al menos una de las condiciones es verdadera usando el operador 'or':
    - Si el usuario es premium o tiene un cupón.
    
    Los resultados de ambas verificaciones se imprimen por separado.
    """
    # Ejercicio 1: Usando el operador 'and'
    a = 5
    b = 10
    resultado_and = (a > 2) and (b < 15)  # Ambas condiciones son verdaderas
    print(f"Resultado de 'and' (ambas condiciones son verdaderas): {resultado_and}")  # Salida: True

    # Ejercicio 2: Usando el operador 'or'
    usuario_premium = False
    tiene_cupon = True
    resultado_or = usuario_premium or tiene_cupon  # Solo una condición necesita ser verdadera
    print(f"Resultado de 'or' (al menos una condición es verdadera): {resultado_or}")  # Salida: True


# Ejecutar la función principal
if __name__ == "__main__":
    verificar_condiciones_logicas()
