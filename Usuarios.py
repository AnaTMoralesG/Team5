# Definimos la clase User
class User:
    def __init__(self, nombre, apellido, password, tipo_usuario):
        self.nombre = nombre
        self.apellido = apellido
        self.password = password
        self.tipo_usuario = tipo_usuario
       

usuarios = {}  # Diccionario para almacenar los usuarios registrados

# Definimos la clase Agente_del_gobierno
class Agente_del_gobierno(User):
    def __init__(self, nombre, apellido, password, tipo_usuario):
     super().__init__(nombre, apellido, password, tipo_usuario)

# Logica para realizar el registro de usuarios si escogen la opción 2
def registrar_usuario():
    print("Registro de Usuario")
    while True:
# por alguna razon si ingreso cualquier caracter que no sea C o A me deja registrar RESOLVER que solo con el caracter C y A funcione de lo contrario que se imrprima el PRINT "Tipo de usuario no válido. Debe ser 'C' para ciudadano o 'A' para agente del gobierno."
        tipo_usuario = input("¿Eres ciudadano (C) o agente del gobierno (A)? (C/A): ").upper()
        if tipo_usuario == 'C' or tipo_usuario == 'A':
            break
        else:
            print("Tipo de usuario no válido. Debe ser 'C' para ciudadano o 'A' para agente del gobierno.")

    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    correo = input("Correo: ")
    password = input("Contraseña: ")

    usuario = User(nombre, apellido, password, tipo_usuario)  # Crea una instancia de la clase User
    usuarios[correo] = usuario
    print("Usuario registrado con éxito.")
# Logica para realizar el inicio de sesión si escogen la opcion 1
def iniciar_sesion():
    print("Iniciar Sesión")
    correo = input("Introduce tu correo: ")
    password = input("Introduce tu contraseña: ")

    if correo in usuarios:
        usuario = usuarios[correo]
        if usuario.password == password:
            usuario.sesion = True
            print("Sesión iniciada con éxito.")
        else:
            print("Contraseña incorrecta.")
    else:
        print("Usuario no encontrado.")
# si el rol es agente puede visualizar dicho reporte Falta la logica
def visualizar_usuarios():
    pass
# IGUAL EL AGENTE DEBE BORRAR A CIUDADANOS ASI QUE SE DEBE HACER UN DEF_BORRAR_CIUDADANOS Y LA LOGICA
# Registro si el rol es agente
def registrar_agente_del_gobierno():
    global usuario_actual
    if usuario_actual.tipo_usuario == 'A':
        print("Registro de Agente del Gobierno")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        correo = input("Correo: ")
        password = input("Contraseña: ")

        usuario = Agente_del_gobierno(nombre, apellido, password, 'A')  # Crea una instancia de Agente_del_gobierno
        usuarios[correo] = usuario
        print("Agente del Gobierno registrado con éxito.") 
