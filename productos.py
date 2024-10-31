productos = []

def añadir_producto():
    nombre = input("Introduce el nombre del producto: ")
    try:
        precio = float(input("Introduce el precio del producto: "))
        cantidad = int(input("Introduce la cantidad del producto: "))
    except ValueError:
        print("Error: El precio debe ser un número y la cantidad un entero.")
        return

    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    productos.append(producto)
    print(f"Producto '{nombre}' añadido exitosamente.")

def ver_productos():
    if not productos:
        print("No hay productos disponibles.")
    else:
        print("\nLista de Productos:")
        for idx, producto in enumerate(productos, start=1):
            print(f"{idx}. Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
        print()

def actualizar_producto():
    ver_productos()
    if not productos:
        return

    try:
        index = int(input("Introduce el número del producto que deseas actualizar: ")) - 1
        if index < 0 or index >= len(productos):
            print("Error: Selección fuera de rango.")
            return

        print("Introduce los nuevos valores (presiona Enter para mantener el valor actual):")
        producto = productos[index]

        nuevo_nombre = input(f"Nombre actual ({producto['nombre']}): ") or producto['nombre']
        nuevo_precio = input(f"Precio actual ({producto['precio']}): ")
        nuevo_precio = float(nuevo_precio) if nuevo_precio else producto['precio']
        nueva_cantidad = input(f"Cantidad actual ({producto['cantidad']}): ")
        nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else producto['cantidad']

        producto.update({"nombre": nuevo_nombre, "precio": nuevo_precio, "cantidad": nueva_cantidad})
        print("Producto actualizado correctamente.")
    except (ValueError, IndexError):
        print("Error en la entrada.")

def eliminar_producto():
    ver_productos()
    if not productos:
        return

    try:
        index = int(input("Introduce el número del producto que deseas eliminar: ")) - 1
        if index < 0 or index >= len(productos):
            print("Error: Selección fuera de rango.")
            return

        eliminado = productos.pop(index)
        print(f"Producto '{eliminado['nombre']}' eliminado.")
    except ValueError:
        print("Error en la entrada.")

def guardar_datos():
    with open("productos.txt", "w") as file:
        for producto in productos:
            file.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Datos guardados en 'productos.txt'.")

def cargar_datos():
    try:
        with open("productos.txt", "r") as file:
            for line in file:
                nombre, precio, cantidad = line.strip().split(",")
                productos.append({"nombre": nombre, "precio": float(precio), "cantidad": int(cantidad)})
        print("Datos cargados correctamente.")
    except FileNotFoundError:
        print("No se encontró un archivo de datos previo, comenzando sin datos.")
    except ValueError:
        print("Error al leer los datos, archivo con formato incorrecto.")


def menu():
    cargar_datos()
    while True:
        print("\nMenú de Gestión de Productos")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            print("Saliendo del programa. Hasta luego!")
            break
        else:
            print("Por favor, selecciona una opción válida.")