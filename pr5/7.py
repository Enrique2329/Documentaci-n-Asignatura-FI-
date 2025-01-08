def sumar_numeros_entre(inicio, fin, metodo):
    """
    Calcula la suma de los números enteros entre dos números dados, utilizando un bucle 'for' o 'while'.

    Parámetros:
    inicio (int): El número inicial.
    fin (int): El número final.
    metodo (str): El método a utilizar para la suma ('for' o 'while').

    Retorna:
    int: La suma de los números entre 'inicio' y 'fin' inclusive, según el método seleccionado.
    """
    if inicio > fin:
        inicio, fin = fin, inicio  # Asegurarse de que 'inicio' sea siempre menor que 'fin'

    suma = 0

    # Sumar usando un bucle 'for'
    if metodo == "for":
        for i in range(inicio, fin + 1):
            suma += i
    # Sumar usando un bucle 'while'
    elif metodo == "while":
        i = inicio
        while i <= fin:
            suma += i
            i += 1
    else:
        print("Método no válido. Elija 'for' o 'while'.")
        suma = None  # Si el método no es válido, se asigna None a la suma

    return suma

# Solicitar entrada al usuario
inicio = int(input("Introduce el número inicial: "))
fin = int(input("Introduce el número final: "))
metodo = input("Selecciona el método ('for' o 'while'): ").strip().lower()

# Llamar a la función y mostrar el resultado
resultado = sumar_numeros_entre(inicio, fin, metodo)

if resultado is not None:
    print(f"La suma de los números entre {inicio} y {fin} es: {resultado}")

