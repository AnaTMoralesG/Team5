class Reporte:
    def __init__(self, nombre_del_reporte, detalles, evidencias, categorias):
        self.nombre_del_reporte = nombre_del_reporte
        self.detalles = detalles
        self.evidencias = evidencias
        self.categorias = categorias

    def mostrar_caracteristicas(self):
        print(f"Nombre del reporte: {self.nombre_del_reporte}")
        print(f"Detalles: {self.detalles}")
        print(f"Categorías: {', '.join(self.categorias)}")

    def eliminar(self):
        print(f"El reporte '{self.nombre_del_reporte}' ha sido eliminado")