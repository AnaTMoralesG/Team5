# Importa las clases y funciones necesarias de los archivos correspondientes
from proyecto_eco_tic.user import User, Agente_del_gobierno
from proyecto_eco_tic.report import Reporte


# Crear un ciudadano
ciudadano1 = User("Juan", "Perez", "clave123", "Ciudadano")
ciudadano1.mostrar_perfil()

# Crear un agente de gobierno
agente1 = Agente_del_gobierno("Maria", "Gomez", "clave456", "Agente_de_gobierno" )
agente1.mostrar_perfil()

# Ciudadano crea un reporte
ciudadano1.crear_reporte("Reporte de Basura", "Mucha basura en la calle", "imagen1.jpg", "Coordenadas XYZ, Calle ABC")
ciudadano1.ver_mis_reportes()

# Agente de gobierno revisa un informe
informe = ciudadano1.reportes[0]
agente1.revisar_informe(informe)
print("Estado del informe:", informe.estado)

# Agente de gobierno resuelve un informe
agente1.resolver_informe(informe)
print("Estado del informe:", informe.estado)