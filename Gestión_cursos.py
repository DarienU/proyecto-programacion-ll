def menu_profesor():
    print("\nBienvenido, profesor.")
    print("1. Ver cursos")
    print("2. Editar curso")
    print("3. Eliminar curso")
    opcion = input("Seleccione una opción: ")
    return opcion

def menu_estudiante():
    print("\nBienvenido, estudiante.")
    print("1. Ver cursos")
    print("2. Inscribirse en un curso")
    opcion = input("Seleccione una opción: ")
    return opcion

def ver_cursos(cursos):
    print("\nLista de cursos:")
    for i, curso in enumerate(cursos):
        print(f"{i+1}. {curso.titulo} - {curso.descripcion} (Profesor: {curso.profesor})")

def editar_curso(cursos):
    ver_cursos(cursos)
    indice = int(input("Ingrese el número del curso que desea editar: ")) - 1
    nuevo_titulo = input("Ingrese el nuevo título del curso: ")
    nuevo_descripcion = input("Ingrese la nueva descripción del curso: ")
    cursos[indice].titulo = nuevo_titulo
    cursos[indice].descripcion = nuevo_descripcion
    print("Curso editado exitosamente.")

def eliminar_curso(cursos):
    ver_cursos(cursos)
    indice = int(input("Ingrese el número del curso que desea eliminar: ")) - 1
    del cursos[indice]
    print("Curso eliminado exitosamente.")

def inscribirse_curso(cursos):
    ver_cursos(cursos)
    indice = int(input("Ingrese el número del curso en el que desea inscribirse: ")) - 1
    print(f"¡Te has inscrito en el curso '{cursos[indice].titulo}'!")