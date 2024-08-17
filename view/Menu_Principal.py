def Menu_Principal():
    """Función para mostrar el menú principal."""

    while True:
        # Mostrar las opciones del menú
        print("-" * 20)
        print("Menú principal")
        print("-" * 20)
        print("1. Gestión de usuarios")
        print("2. Gestión de cursos")
        print("3. Gestión de calificaciones")
        print("4. Salir")

        # Obtener la opción del usuario
        opcion = int(input("Seleccione una opción: "))

        # Validar la entrada del usuario
        if opcion not in range(1, 5):
            print("Opción no válida. Inténtalo de nuevo.")
            continue
