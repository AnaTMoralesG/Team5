class Notificaciones:
  
   contador_id = 0

   def __init__(self, mensaje):
      Notificaciones.contador_id += 1

      self.id = Notificaciones.contador_id
     
      self.mensaje = mensaje
   
   def notificaciones(reporte, mensaje):
    reporte.ciudadano.recibir_notificacion(mensaje)