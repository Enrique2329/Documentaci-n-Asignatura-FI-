
def registrar_persona():
    """
    Solicita los datos de una persona, como nombre, apellidos, edad y estatura,
    y luego muestra la información ingresada.

    La función no toma parámetros ni devuelve valores. Solicita la entrada del
    usuario a través de la consola y muestra los resultados en formato legible.

    Ejemplo de ejecución:
        Introduce tu nombre: John
        Introduce tus apellidos: Doe
        Introduce tu edad: 30
        Introduce tu estatura (en metros): 1.75

    Salida:
        Información de la persona:
        Nombre: John
        Apellidos: Doe
        Edad: 30 años
        Estatura: 1.75 metros
    """
    # Solicitar datos de la persona
    nombre = input("Introduce tu nombre: ")
    apellidos = input("Introduce tus apellidos: ")
    edad = input("Introduce tu edad: ")
    estatura = input("Introduce tu estatura (en metros): ")

    # Mostrar la información de la persona
    print("\nInformación de la persona:")
    print(f"Nombre: {nombre}")
    print(f"Apellidos: {apellidos}")
    print(f"Edad: {edad} años")
    print(f"Estatura: {estatura} metros")


if __name__ == "__main__":
    # Llamada a la función para registrar a la persona
    registrar_persona()
