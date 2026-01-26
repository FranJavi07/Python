"""
He creado un proyecto sobre un restaurante de la forma mas simple posible pero que nos
permite  añadir, buscar, modificar, eliminar y mostrar platos.
"""
menu = []


def insertar_elemento(datos):
    """
    Añade un plato al menú.

    Pide los datos al usuario y los guarda en la lista.

    Args:
        datos (list): Lista del menú.
    """
    try:
        id_plato = int(input("ID del plato: "))
        nombre = input("Nombre del plato: ")
        precio = float(input("Precio del plato: "))

        plato = {
            "id": id_plato,
            "nombre": nombre,
            "precio": precio
        }

        datos.append(plato)
        print("Plato añadido correctamente.")

    except:
        print("Error: datos incorrectos.")


def buscar_elemento(datos):
    """
    Busca un plato por su ID y lo muestra.

    Args:
        datos (list): Lista del menú.
    """
    try:
        id_buscar = int(input("ID del plato a buscar: "))

        for plato in datos:
            if plato["id"] == id_buscar:
                print(plato)
                return

        print("Plato no encontrado.")

    except:
        print("Error al buscar el plato.")


def modificar_elemento(datos):
    """
    Modifica el precio de un plato.

    Args:
        datos (list): Lista del menú.
    """
    try:
        id_modificar = int(input("ID del plato a modificar: "))

        for plato in datos:
            if plato["id"] == id_modificar:
                nuevo_precio = float(input("Nuevo precio: "))
                plato["precio"] = nuevo_precio
                print("Plato modificado.")
                return

        print("Plato no encontrado.")

    except:
        print("Error al modificar el plato.")


def eliminar_elemento(datos):
    """
    Elimina un plato del menú.

    Args:
        datos (list): Lista del menú.
    """
    try:
        id_eliminar = int(input("ID del plato a eliminar: "))

        for plato in datos:
            if plato["id"] == id_eliminar:
                datos.remove(plato)
                print("Plato eliminado.")
                return

        print("Plato no encontrado.")

    except:
        print("Error al eliminar el plato.")


def mostrar_todos(datos):
    """
    Muestra todos los platos del menú.

    Args:
        datos (list): Lista del menú.
    """
    if datos == []:
        print("El menú está vacío.")
    else:
        for plato in datos:
            print(plato)


def menu_principal():
    """
    Muestra el menú y controla el programa.
    """
    opcion = ""

    while opcion != "6":
        print("""
1. Añadir plato
2. Buscar plato
3. Modificar plato
4. Eliminar plato
5. Mostrar menú
6. Salir
        """)

        opcion = input("Elige una opción: ")

        if opcion == "1":
            insertar_elemento(menu)
        elif opcion == "2":
            buscar_elemento(menu)
        elif opcion == "3":
            modificar_elemento(menu)
        elif opcion == "4":
            eliminar_elemento(menu)
        elif opcion == "5":
            mostrar_todos(menu)
        elif opcion == "6":
            print("Saliendo del programa...")
        else:
            print("Opción incorrecta.")


menu_principal()
