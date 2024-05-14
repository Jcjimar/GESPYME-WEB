import json

class Usuario:
    def __init__(self, id_usuario, nombre_usuario, contrasena_usuario, tipo_usuario):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.contrasena_usuario = contrasena_usuario
        self.tipo_usuario = tipo_usuario

    def __repr__(self) -> str:
        return f"Usuario(id_usuario={self.id_usuario}, nombre_usuario={self.nombre_usuario}, contrasena_usuario={self.contrasena_usuario}, tipo_usuario = {self.tipo_usuario})"
    
    @classmethod
    def from_json(cls, json_data):
        return cls(json_data['id_usuario'], json_data['nombre_usuario'], json_data['contrasena_usuario', json_data['tipo_usuario']])
    
# Función para cargar datos desde un archivo JSON y convertirlos en objetos Usuario
def cargar_usuarios_desde_json(data):
    with open(data, 'r') as dt:
        datos_json = json.load(dt)
        return [Usuario.from_json(usuario) for usuario in datos_json]

# Función para guardar datos (objetos Usuario) en un archivo JSON
def guardar_usuarios_en_json(usuarios, data):
    datos_json = [usuario.__dict__ for usuario in usuarios]
    with open(data, 'w') as dt:
        json.dump(datos_json, dt, indent=4)

# Ejemplo de uso
if __name__ == "__main__":
    # Cargar datos desde el archivo JSON
    usuarios = cargar_usuarios_desde_json('data.json')

    # Imprimir los usuarios cargadas
    for usuario in usuarios:
        print(usuario)

    # Modificar un usuario (por ejemplo, cambiar el nombre de usuario)
    usuarios[0].nombre_usuario = "Antonio"

    # Guardar las películas modificadas de vuelta al archivo JSON
    guardar_usuarios_en_json(usuarios, 'data.json')
    
