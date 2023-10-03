class Location:
    def __init__(self, id_ubicacion,coordenadas, nombre_lugar):
        self.id_ubicacion = id_ubicacion
        self.coordenadas = coordenadas
        self.nombre_lugar = nombre_lugar

    def mostrar_ubicacion(self):
        print("Nombre del lugar: {self.nombre_lugar}")
        print("Coordenadas de la ubicación: {self.coordenadas}")


