class Notificaciones:
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def notificar_ciudadano(reporte, mensaje):
        reporte.ciudadano.recibir_notificacion(mensaje)