class User:
    def __init__(self, nombre, apellido, password, tipo_usuario):
        self.nombre = nombre
        self.apellido = apellido
        self.password = password
        self.tipo_usuario = tipo_usuario
        self.reportes = []
        self.notificaciones = []

    def mostrar_perfil(self):
        print(f"Perfil de ciudadano: {self.nombre} {self.apellido}")

    def recibir_notificacion(self, mensaje):
        self.notificaciones.append(mensaje)
        print("Notificación recibida:", mensaje)

    def ver_mis_reportes(self):
        print("Mis reportes:")
        for reporte in self.reportes:
            reporte.mostrar_caracteristicas()

    def crear_reporte(self, nombre_del_reporte, detalles, evidencias, categorias):
        reporte = reporte(nombre_del_reporte, detalles, evidencias, categorias)
        self.reportes.append(reporte)
        print("Reporte creado")

    def eliminar_reporte(self, reporte):
        if reporte in self.reportes:
            self.reportes.remove(reporte)
            reporte.eliminar()
            print("Reporte eliminado")
        else:
            print("El reporte no ha sido encontrado")

class Agente_del_gobierno(User):
    def __init__(self, nombre, apellido, password, tipo_usuario):
        super().__init__(nombre, apellido, password, tipo_usuario)

    def mostrar_perfil(self):
        print(f"Perfil de agente de gobierno: {self.nombre} {self.apellido},")

    def revisar_informe(self, reporte):
        reporte.estado = "En revisión"
        self.informes_pendientes.append(reporte)

    def resolver_informe(self, reporte):
        reporte.estado = "Resuelto"
        self.informes_pendientes.remove(reporte)

    def notificar_ciudadanos(self, reporte):
        mensaje = f"El informe '{reporte.nombre_del_reporte}' ha sido actualizado. Nuevo estado: {reporte.estado}"
        reporte.ciudadano.recibir_notificacion(mensaje)

