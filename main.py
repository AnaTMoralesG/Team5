from user import User, Agente_del_gobierno
from report import Reporte
from categories import Categorias
from search import sqeadr
from notification import Notificacion

#init values
usuario = Agente_del_gobierno("Ana", "montes", "123", "Agente_de_gobierno")
User.registrarse(User)
User.crear_categoria("Contaminación del agua", "Toda contaminación o basura en cuerpos de agua")
User.crear_categoria("Deforestación", "Tala irregular de los árboles de la zona")
User.crear_categoria("Contaminación del suelo", "Cualquier desperdicio que se este acumulando en el suelo")
0
usuario = User("Carlos", "Gomez", "456", "Ciudadano" )
User.registrarse(usuario)
User.crear_reporte("Lago seco", "El nivel del agua ha bajado ultimamente", ["foto1"], "El lago más grande de la zona", Categoria.categorias[0])
User.crear_reporte("Basura acumulada", "En la ultima semana el camión de la basura no ha pasado", ["foto1", "foto2"], "Entre calles x y x", Categoria.categorias[2])
# ..

def menu_principal():
    print("\n-- Menú Principal --")
    print("1. Iniciar Sesión")0
    
    print("2. Registrarse")
    print("3. Salir")
    eleccion = input("Seleccione una opción: ")
    return eleccion

def menu_ciudadano():
    print("\n-- Menú Ciudadano --")
    print("1. Crear Reporte")
    print("2.  Reportes")
    print("3. Editar Reporte")
    print("4. Borrar Reporte")
    print("5. Buscar Reportes")
    print("6. Ver Notificaciones")  # Añadido
    print("7. Ver Perfil")
    print("8. Cerrar sesion")  # Cambiado a opción 8
    eleccion = input("Seleccione una opción: ")
    return eleccion


def menu_servidor_publico():
    print("\n-- Menú Servidor Público --")
    print("1. Cambiar Estatus de Reporte")
    print("2. Crear Categoría")
    print("3. Ver Notificaciones")
    print("4. Borrar Categoría")
    print("5. Editar Categoría")
    print("6. Ver Perfil")
    print("7. Cerrar Sesión")
    eleccion = input("Seleccione una opción: ")
    return eleccion

def main():
    while True:
        eleccion = menu_principal()
        if eleccion == "1":  # Iniciar Sesión
            correo = input("Introduce tu correo: ")
            password = input("Introduce tu contraseña: ")
            usuario = User.iniciar_sesion(correo, password)
            if usuario:
                while User.sesion:
                    if isinstance(usuario, User):
                        eleccion_ciudadano = menu_ciudadano()

                        # Crear Reporte
                        if eleccion_ciudadano == "1":
                            titulo = input("Título del reporte: ")
                            descripcion = input("Descripción: ")
                            fotos = input("Fotos (separadas por comas): ").split(',')
                            Referencias = input("Referencias: ")
                            print("Categorías disponibles:")
                            for index, categoria in enumerate(Categoria.categorias, 1):
                                print(f"{index}. {categoria.nombre}")
                            while True:
                                eleccion_categoria = int(input("Seleccione una categoría por número: "))
                                if eleccion_categoria < len(Categoria.categorias) and eleccion_categoria > 0:
                                    categoria_seleccionada = Categoria.categorias[eleccion_categoria - 1]
                                    break
                                else:
                                    print("La opción no existe")                                    
                            
                            usuario.crear_reporte(titulo, descripcion, fotos, Referencias, categoria_seleccionada)
                            print("Reporte creado con éxito!")
                            
                        # Ver mis Reportes
                        elif eleccion_ciudadano == "2":
                            usuario.listar_mis_reportes()
                            
                        # Editar Reporte
                        elif eleccion_ciudadano == "3":
                            print("\Reportes")
                            print("0. Cancelar")
                            for index, reporte in enumerate(usuario.reportes, 1):
                                print(f"{index}. {reporte.titulo}")

                            while True:
                                reporte_id = int(input("Seleccione el reporte a editar: "))
                                if 0 < reporte_id <= len(usuario.reportes):
                                    nuevo_titulo = input("Nuevo título: ")
                                    Reporte.editar(usuario.reportes[reporte_id-1].id, nuevo_titulo)
                                    break
                                elif reporte_id == 0:
                                    break
                                else:
                                    print("La opción no existe")
                        # Borrar Reporte
                        elif eleccion_ciudadano == "4":
                            print("\Reportes")
                            print("0. Cancelar")
                            for index, reporte in enumerate(usuario.reportes, 1):
                                print(f"{index}. {reporte.titulo}")

                            while True:
                                reporte_id = int(input("Seleccione el reporte a borrar: "))
                                if 0 < reporte_id <= len(usuario.reportes):
                                    usuario.eliminar_reporte(usuario.reportes[reporte_id-1])
                                    break
                                elif reporte_id == 0:
                                    break
                                else:
                                    print("La opción no existe")
                                
                        # Buscar Reportes
                        elif eleccion_ciudadano == "5":
                            termino_busqueda = input("Ingrese el término de búsqueda: ")

                            print("\nCategorías disponibles:")
                            print("0. Ninguna categoría")
                            for index, categoria in enumerate(Categoria.categorias, 1):
                                print(f"{index}. {categoria.nombre}")

                            while True:
                                eleccion_categoria = int(input("Seleccione una categoría por número: "))
                                if 0 <= eleccion_categoria <= len(Categoria.categorias):
                                    categoria_seleccionada = "" if eleccion_categoria == 0 else Categoria.categorias[eleccion_categoria - 1].nombre
                                    buscador = Busqueda(termino_busqueda, categoria_seleccionada)
                                    buscador.filtrar()
                                    buscador.listar_busqueda()
                                    break
                                else:
                                    print("La opción no existe")

                                
                        # Ver Notificaciones
                        elif eleccion_ciudadano == "6":
                            usuario.revisar_notificaciones()

                        # Ver Perfil
                        elif eleccion_ciudadano == "7":
                            usuario.mostrar_perfil()     

                        # Cerrar Sesión
                        elif eleccion_ciudadano == "8":
                            usuario.cerrar_sesion()
                                                
                    elif isinstance(usuario, Agente_del_gobierno):
                            eleccion_servidor = menu_servidor_publico()
                            # Cambiar Estatus de Reporte
                            if eleccion_servidor == "1":
                                    reporte_id = int(input("ID del reporte a cambiar: "))
                                    nuevo_status = input("Nuevo estatus: ")
                                    usuario.cambiar_estatus_reporte(reporte_id, nuevo_status)
                                                                        
                                # Crear Categoría
                            elif eleccion_servidor == "2":
                                nombre_categoria = input("Nombre de la nueva categoría: ")
                                descripcion_categoria = input("Descripción: ")
                                usuario.crear_categoria(nombre_categoria, descripcion_categoria)
                                print(f"Categoría '{nombre_categoria}' creada con éxito!")
                                
                                # Ver Notificaciones
                            elif eleccion_servidor == "3":
                                notificaciones = usuario.notificaciones
                                for notif in notificaciones:
                                    print(notif)
                                        # Borrar Categoría
                            elif eleccion_servidor == "4":
                                nombre_categoria = input("Nombre de la categoría a borrar: ")
                                Categoria.borrar_categoria(nombre_categoria)
                                    
                            elif eleccion_servidor == "5":  # Editar Categoría
                                nombre_actual = input("Nombre actual de la categoría: ")
                                nuevo_nombre = input("Nuevo nombre: ")

                                # Buscar el id de la categoría por el nombre actual
                                categoria_id = None
                                for cat in Categoria.categorias:
                                    if cat.nombre == nombre_actual:
                                        categoria_id = cat.id
                                        break
                                
                                if categoria_id:
                                    Categoria.editar_categoria(categoria_id, nuevo_nombre)
                                else:
                                    print("Categoría no encontrada")
                            # Ver Perfil
                            elif eleccion_servidor == "6":
                                usuario.mostrar_perfil()
                                # Cerrar Sesión
                            elif eleccion_servidor == "7":
                                usuario.cerrar_sesion()

        elif eleccion == "2":  # Registrarse
            print("Registro de Usuario")
            tipo = input("¿Eres ciudadano o servidor público? (C/S): ").upper()
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            correo = input("Correo: ")
            password = input("Contraseña: ")
            estatus = "Activo"
            
            if tipo == "C":  # Ciudadano
                telefono = input("Teléfono: ")
                nuevo_usuario = User(nombre, apellido, correo, password, estatus, telefono)
                User.registrarse(nuevo_usuario)
            elif tipo == "S":  # Servidor Público
                rol = input("Rol: ")
                nuevo_usuario = Agente_del_gobierno(nombre, apellido, correo, password, estatus, rol)
                User.registrarse(nuevo_usuario)
            else:
                print("Tipo de usuario no válido.")
            continue  # Salta a la siguiente iteración del bucle

        elif eleccion == "3":  # Salir
            print("¡Gracias por usar nuestra aplicación!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

