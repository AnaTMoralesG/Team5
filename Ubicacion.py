class Ubicacion:
    def __init__(self, id_ubicacion, coordenadas, nombre_lugar):
        self.id_ubicacion = id_ubicacion
        self.coordenadas = coordenadas
        self.nombre_lugar = nombre_lugar

    def mostrar_ubicacion(self):
        print(f"Nombre del lugar: {self.nombre_lugar}")

        print(f"Coordenadas de la ubicación: {self.coordenadas}")

        print(f"Coordenadas de la ubicación: {self.coordenadas}")
