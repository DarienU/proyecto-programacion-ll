import json


def LeerUsuarios():
    """Función para leer el archivo JSON de usuarios."""
    with open("./model/usuarios.json", "r") as f:
        usuarios = json.load(f)
    return usuarios
