from categories import Categorias  # Importa la clase Categorias desde el archivo categorias.py

class Busqueda:

    contador_id = 0

    def _init_(self):
        Busqueda.contador_id += 1

        self.id = Busqueda.contador_id
        self.categorias = Categorias()

    def seleccionar_categoria(self):
        while True:
            try:
                self.categorias.mostrar_categorias()
                opcion = int(input("Selecciona una categoría (1-4) o 0 para salir: "))
                if opcion == 1:
                    self.categorias.categoria_1()
                elif opcion == 2:
                    self.categorias.categoria_2()
                elif opcion == 3:
                    self.categorias.categoria_3()
                elif opcion == 4:
                    self.categorias.categoria_4()
                elif opcion == 0:
                    print("Hasta luego. ¡Adiós!")
                    break
                else:
                    print("Por favor, selecciona una opción válida (1-4) o 0 para salir.")
            except ValueError:
                print("Por favor, ingresa un número válido.")

if _name_ == "_main_":
    busqueda = Busqueda()
    busqueda.seleccionar_categoria()