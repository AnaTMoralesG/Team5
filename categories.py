class Categorias:
    def _init_(self):
        self.opcion = 0

    def mostrar_categorias(self):
        print("1. Categoría 1")
        print("2. Categoría 2")
        print("3. Categoría 3")
        print("4. Categoría 4")

    def categoria_1(self):
        print("Bienvenido a la Categoría 1")
        # Lógica y funcionalidades para la Categoría 1

    def categoria_2(self):
        print("Bienvenido a la Categoría 2")
        # Lógica y funcionalidades para la Categoría 2

    def categoria_3(self):
        print("Bienvenido a la Categoría 3")
        # Lógica y funcionalidades para la Categoría 3

    def categoria_4(self):
        print("Bienvenido a la Categoría 4")
        # Lógica y funcionalidades para la Categoría 4

    def seleccionar_categoria(self):
        while True:
            try:
                self.mostrar_categorias()
                self.opcion = int(input("Selecciona una categoría (1-4) o 0 para salir: "))
                if self.opcion == 1:
                    self.categoria_1()
                elif self.opcion == 2:
                    self.categoria_2()
                elif self.opcion == 3:
                    self.categoria_3()
                elif self.opcion == 4:
                    self.categoria_4()
                elif self.opcion == 0:
                    print("Hasta luego. ¡Adiós!")
                    break
                else:
                    print("Por favor, selecciona una opción válida (1-4) o 0 para salir.")
            except ValueError:
                print("Por favor, ingresa un número válido.")

# Crear una instancia de la clase Categorias
categorias = Categorias()

# Llamar al método seleccionar_categoria de la instancia
categorias.seleccionar_categoria()