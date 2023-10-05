class Ubicacion:

    contador_id = 0

    def __init__(self, id_ubicacion, coordenadas, nombre_lugar):
        Ubicacion.contador_id += 1
        
        self.id = Ubicacion.contador_id
        self.coordenadas = coordenadas
        self.nombre_lugar = nombre_lugar

    def mostrar_ubicacion(self):
        print(f"Nombre del lugar: {self.nombre_lugar}")

        print(f"Coordenadas de la ubicación: {self.coordenadas}")

        print(f"Coordenadas de la ubicación: {self.coordenadas}")
