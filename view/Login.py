from controller.LeerUsuarios import LeerUsuarios
# from view.Menu_Principal import Menu_Principal
from getpass import getpass

usuarios = LeerUsuarios()


def Login():
    """Función para mostrar la pantalla de login."""

    # Mensaje de bienvenida
    print("Bienvenido al sistema de gestión académica GIRASOL")

    # Solicitar nombre de usuario y contraseña
    username = input("Nombre de usuario: ")
    password = getpass("Contraseña: ")

    # Buscar el usuario en el archivo JSON
    usuario = next((u for u in usuarios if u["username"] == username), None)

    # Validar las credenciales
    if usuario and usuario["password"] == password:
        print("Acceso concedido")
        # Iniciar sesión y mostrar el menú principal
        # Menu_Principal()
    else:
        print("Credenciales incorrectas. Inténtalo de nuevo.")
        Login()
