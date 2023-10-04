def mostrar_categorias():
    print("1. Categoría 1")
    print("2. Categoría 2")
    print("3. Categoría 3")
    print("4. Categoría 4")

def categoria_1():
    print("Bienvenido a la Categoría 1")
    # Lógica y funcionalidades para la Categoría 1

def categoria_2():
    print("Bienvenido a la Categoría 2")
    # Lógica y funcionalidades para la Categoría 2

def categoria_3():
    print("Bienvenido a la Categoría 3")
    # Lógica y funcionalidades para la Categoría 3

def categoria_4():
    print("Bienvenido a la Categoría 4")
    # Lógica y funcionalidades para la Categoría 4

def seleccionar_categoria():
    while True:
        try:
            opcion = int(input("Selecciona una categoría (1-4) o 0 para salir: "))
            if opcion == 1:
                categoria_1()
            elif opcion == 2:
                categoria_2()
            elif opcion == 3:
                categoria_3()
            elif opcion == 4:
                categoria_4()
            elif opcion == 0:
                print("Hasta luego. ¡Adiós!")
                break
            else:
                print("Por favor, selecciona una opción válida (1-4) o 0 para salir.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

mostrar_categorias()
seleccionar_categoria()