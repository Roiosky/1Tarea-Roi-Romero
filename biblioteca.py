# Diccionario inicial de la biblioteca
biblioteca = {
    "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "disponible": True},
    "1984": {"autor": "George Orwell", "año": 1949, "disponible": True},
    "El principito": {"autor": "Antoine de Saint-Exupéry", "año": 1943, "disponible": False}
}

# Función para agregar un nuevo libro a la biblioteca
def agregar_libro():
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    año = int(input("Ingrese el año de publicación del libro: "))
    biblioteca[titulo] = {"autor": autor, "año": año, "disponible": True}
    print(f'El libro "{titulo}" ha sido agregado a la biblioteca.')

# Función para prestar un libro (marcarlo como no disponible)
def prestar_libro():
    titulo = input("Ingrese el título del libro que desea prestar: ")
    if titulo in biblioteca:
        if biblioteca[titulo]["disponible"]:
            biblioteca[titulo]["disponible"] = False
            print(f'El libro "{titulo}" ha sido prestado.')
        else:
            print(f'El libro "{titulo}" ya está prestado.')
    else:
        print(f'El libro "{titulo}" no se encuentra en la biblioteca.')

# Función para devolver un libro (marcarlo como disponible)
def devolver_libro():
    titulo = input("Ingrese el título del libro que desea devolver: ")
    if titulo in biblioteca:
        if not biblioteca[titulo]["disponible"]:
            biblioteca[titulo]["disponible"] = True
            print(f'El libro "{titulo}" ha sido devuelto.')
        else:
            print(f'El libro "{titulo}" ya está disponible.')
    else:
        print(f'El libro "{titulo}" no se encuentra en la biblioteca.')

# Función para mostrar todos los libros en la biblioteca
def mostrar_libros():
    for titulo, info in biblioteca.items():
        estado = "Disponible" if info["disponible"] else "No disponible"
        print(f'Título: {titulo}, Autor: {info["autor"]}, Año: {info["año"]}, Estado: {estado}')

# Función para mostrar los libros publicados en un año específico
def mostrar_libros_por_año():
    año = int(input("Ingrese el año de publicación para ver los libros: "))
    encontrados = False
    for titulo, info in biblioteca.items():
        if info["año"] == año:
            estado = "Disponible" if info["disponible"] else "No disponible"
            print(f'Título: {titulo}, Autor: {info["autor"]}, Estado: {estado}')
            encontrados = True
    if not encontrados:
        print(f"No se encontraron libros publicados en el año {año}.")

# Menú principal
def menu():
    while True:
        print("\n--- Menú de la Biblioteca ---")
        print("1. Agregar un nuevo libro")
        print("2. Prestar un libro")
        print("3. Devolver un libro")
        print("4. Ver todos los libros")
        print("5. Ver libros por año de publicación")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            prestar_libro()
        elif opcion == "3":
            devolver_libro()
        elif opcion == "4":
            mostrar_libros()
        elif opcion == "5":
            mostrar_libros_por_año()
        elif opcion == "6":
            print("Gracias por usar el gestor de biblioteca. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# Ejecución del menú
menu()
