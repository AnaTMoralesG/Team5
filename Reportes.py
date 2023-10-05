from Ubicacion import Ubicacion

class Reporte:

    contador_id = 0

    def __init__(self, nombre_del_reporte, detalles, evidencias, categorias):
        
        Reporte.contador_id += 1
        
        self.id = Reporte.contador_id
        print(f"{Reporte.id}")

        self.nombre_del_reporte = nombre_del_reporte
        self.detalles = detalles
        self.evidencias = evidencias
        self.categorias = categorias
        self.Ubicacion = Ubicacion()

reporte = {} # biblioteca
# se despliega la logica para crear el reporte que luego se importara en Main.py
def crear_reporte():
    global usuario_actual
    # si el rol es ciudadano puede crear reporte
    if usuario_actual.tipo_usuario == 'C':
        nombre_del_reporte = input("Nombre del reporte: ")
        detalles = input("Detalles del reporte: ")
        evidencias = input("Evidencias: ")
        categorias = input("Categorías (separadas por comas): ").split(",")

        nuevo_reporte = Reporte(nombre_del_reporte, detalles, evidencias, categorias)
        reporte[nombre_del_reporte] = nuevo_reporte

        print("Reporte creado con éxito.")
# si el rol es agente puede visualizar dicho reporte 
def visualizar_reporte():
    global usuario_actual
    if usuario_actual.tipo_usuario == 'A':
        nombre_reporte = input("Ingrese el nombre del reporte a visualizar: ")
        if nombre_reporte in reporte:
            reporte_obj = reporte[nombre_reporte]
            print(f"Nombre del reporte: {reporte_obj.nombre_del_reporte}")
            print(f"Detalles: {reporte_obj.detalles}")
            print(f"Categorías: {', '.join(reporte_obj.categorias)}")
        else:
            print("El reporte no existe.")
# si el rol es agente puede borrar  dicho reporte PERO EN EL DIAGRAMA 
# NO APARECE SI EL CIUDADANO PUEDE ELIMINAR EL REPORTE ASI QUE N OSE SI PONERLO 
def eliminar_reporte():
    global usuario_actual
    if usuario_actual.tipo_usuario == 'A':
        nombre_reporte = input("Ingrese el nombre del reporte a eliminar: ")
        if nombre_reporte in reporte:
            del reporte[nombre_reporte]
            print(f"El reporte '{nombre_reporte}' ha sido eliminado.")
        else:
            print("El reporte no existe.")
# DE IGUAL MANERA NO SE SI SE AGREGA EDITAR O ACTUALZIAR REPORTE YA QUE EN EL DIAGRMAMA NO APARECE