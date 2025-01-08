def estadisticas_numeros():
    """
    Solicita al usuario una serie de números y calcula las estadísticas más relevantes:
    el número más grande, el más pequeño y la media.
    
    El proceso termina cuando el usuario ingresa 0. El número 0 no se incluye en los cálculos.
    
    La función muestra por pantalla:
    - El número más grande
    - El número más pequeño
    - La media de los números ingresados
    """
    
    print("Introduce números para calcular estadísticas. Ingresa 0 para terminar.")
    
    numeros = []  # Lista para almacenar los números ingresados por el usuario

    while True:
        try:
            # Solicitar un número al usuario
            numero = float(input("Introduce un número: "))
        except ValueError:
            # Si el usuario ingresa algo que no es un número, se muestra un mensaje y se repite el ciclo
            print("Por favor, introduce un número válido.")
            continue
        
        if numero == 0:  # Si el usuario ingresa 0, se termina el ciclo
            break
        
        numeros.append(numero)  # Añadir el número ingresado a la lista
    
    if numeros:  # Verificar si la lista contiene números
        # Calcular el número más grande, más pequeño y la media
        mayor = max(numeros)
        menor = min(numeros)
        media = sum(numeros) / len(numeros)
        
        # Mostrar las estadísticas
        print(f"Número más grande: {mayor}")
        print(f"Número más pequeño: {menor}")
        print(f"Media de los números: {media:.2f}")
    else:
        print("No se ingresaron números para calcular estadísticas.")

# Llamada a la función para ejecutar el programa
estadisticas_numeros()
