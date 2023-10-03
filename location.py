class Location:
    def __init__(self, coordenadas, nombre_lugar):
        self.coordenadas = coordenadas
        self.nombre_lugar = nombre_lugar

    def mostrar_ubicacion(self):
        print("Nombre del lugar: {self.nombre_lugar}")
        print("Coordenadas de la ubicación: {self.coordenadas}")


