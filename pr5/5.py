def menu_principal():
    """
    Muestra un menú interactivo al usuario con diferentes opciones. Según la opción seleccionada,
    se muestra un mensaje indicando la acción seleccionada o un mensaje de error si la opción no es válida.

    El menú tiene las siguientes opciones:
    1. Cargar fichero de datos
    2. Almacenar fichero de datos
    3. Modificar datos
    4. Salir
    
    El programa seguirá mostrando el menú hasta que el usuario elija la opción 'Salir'.
    """
    while True:  # Bucle iterativo para mantener el menú activo hasta seleccionar "Salir"
        # Mostrar las opciones del menú
        print("\nMenu Principal")
        print("1. Cargar fichero de datos")
        print("2. Almacenar fichero de datos")
        print("3. Modificar datos")
        print("4. Salir")
        
        # Solicitar la opción del usuario
        opcion = input("Dime tu opción: ")
        
        # Evaluar la opción seleccionada y mostrar el mensaje correspondiente
        if opcion == "1":
            print("\nHas seleccionado: Cargar fichero de datos")
        elif opcion == "2":
            print("\nHas seleccionado: Almacenar fichero de datos")
        elif opcion == "3":
            print("\nHas seleccionado: Modificar datos")
        elif opcion == "4":
            print("\nSaliendo del programa... ¡Hasta luego!")
            break  # Termina el bucle y sale del menú
        else:
            print("\nEsta opción no está disponible. Inténtalo de nuevo.")  # Mensaje si la opción no es válida

# Llamada a la función para mostrar el menú
menu_principal()
