from Usuarios import User, usuarios, iniciar_sesion, registrar_usuario, registrar_agente_del_gobierno, visualizar_usuarios
from Reportes import Reporte, reporte, visualizar_reporte, crear_reporte, eliminar_reporte
from Categorias import Categorias, categorias
from Buscar import Busqueda
from Notificaciones import notificaciones
from Ubicacion import Ubicacion
# Define una variable global para almacenar el usuario actualmente en sesión
usuario_actual = None

if __name__ == "__main__":
    while True:
        print("\n-- Menú Principal --")
        print("1. Iniciar Sesión")
        print("2. Registrarse como Ciudadano")
        print("3. Registrarse como Agente del Gobierno")
        print("4. Salir")
        eleccion = input("Seleccione una opción: ")

        if eleccion == "1":
            iniciar_sesion()
            if usuario_actual:
            mostrar_menu_segun_rol()
        elif eleccion == "2":
            registrar_usuario()
        elif eleccion == "3":
            registrar_agente_del_gobierno()
        elif eleccion == "4":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def mostrar_menu_segun_rol():
    global usuario_actual

    if usuario_actual.tipo_usuario == 'C':
        menu_ciudadano()
    elif usuario_actual.tipo_usuario == 'A':
        menu_agente_gobierno()
# menu que le aparecera a los usuarios con rol ciudadano
def menu_ciudadano():
    while True:
        print("\n-- Menú Ciudadano --")
        print("1. Crear reporte")
        print("2. Categorías")
        print("3. Buscar")
        print("4. Mis notificaciones")
        print("5. Salir")
        eleccion = input("Seleccione una opción: ")
# se despliega la logica que esta en Reportes.py crear_reporte
        if eleccion == "1":
            crear_reporte()
# se despliega la logica que esta en Categorias.py categorias
        elif eleccion == "2":
            categorias()
# se despliega la logica que esta en Buscar.py buscar
        elif eleccion == "3":
            buscar()
# se despliega la logica que esta en notificaciones.py notificaciones
        elif eleccion == "4":
            notificaciones()
        elif eleccion == "5":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
# Menu que le aparecera a los usuarios con rol agente
def menu_agente_gobierno():
    while True:
        print("\n-- Menú Agente del Gobierno --")
        print("1. Ver reportes")
        print("2. Ver usuarios")
        print("3. Categorías")
        print("4. Buscar")
        print("5. Salir")
        eleccion = input("Seleccione una opción: ")
# se despliega la logica que esta en Reportes.py visualizar_reporte
        if eleccion == "1":
            visualizar_reporte()
# se despliega la logica que esta en Usuarios.py visualizar_usuarios
        elif eleccion == "2":
            visualizar_usuarios()
# se despliega la logica que esta en Categorias.py categorias
        elif eleccion == "3":
            categorias()
# se despliega la logica que esta en Buscar.py buscar
        elif eleccion == "4":
            buscar()
        elif eleccion == "5":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

#Falta las notificaciones
#Falta buscar no funciono el codigo 
#falta lograr que la ubicacion se quede grabada en el reporte
#falta que la busqueda funcione por categorias o nombre de 
#falta que el ID me lo genere en automatico y no que sea manual para ciudadanos,agentes,reportes,categorias y notificaciones