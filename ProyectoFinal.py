"""
He creado un proyecto sobre un restaurante de la forma mas simple posible pero que nos
permite  añadir, buscar, modificar, eliminar y mostrar platos.
"""


class Restaurante:
    """
    Clase que representa un restaurante.

    Guarda un menú y permite gestionarlo.
    """

    def __init__(self):
        """
        Inicializa el restaurante con un menú vacío.
        """
        self.menu = []

    def insertar_elemento(self):
        """
        Añade un plato al menú.

        Pide los datos al usuario y los guarda en la lista.
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

            self.menu.append(plato)
            print("Plato añadido correctamente.")

        except:
            print("Error: datos incorrectos.")

    def buscar_elemento(self):
        """
        Busca un plato por su ID y lo muestra.
        """
        try:
            id_buscar = int(input("ID del plato a buscar: "))

            for plato in self.menu:
                if plato["id"] == id_buscar:
                    print(plato)
                    return

            print("Plato no encontrado.")

        except:
            print("Error al buscar el plato.")

    def modificar_elemento(self):
        """
        Modifica el precio de un plato.
        """
        try:
            id_modificar = int(input("ID del plato a modificar: "))

            for plato in self.menu:
                if plato["id"] == id_modificar:
                    nuevo_precio = float(input("Nuevo precio: "))
                    plato["precio"] = nuevo_precio
                    print("Plato modificado.")
                    return

            print("Plato no encontrado.")

        except:
            print("Error al modificar el plato.")

    def eliminar_elemento(self):
        """
        Elimina un plato del menú.
        """
        try:
            id_eliminar = int(input("ID del plato a eliminar: "))

            for plato in self.menu:
                if plato["id"] == id_eliminar:
                    self.menu.remove(plato)
                    print("Plato eliminado.")
                    return

            print("Plato no encontrado.")

        except:
            print("Error al eliminar el plato.")

    def mostrar_todos(self):
        """
        Muestra todos los platos del menú.
        """
        if self.menu == []:
            print("El menú está vacío.")
        else:
            for plato in self.menu:
                print(plato)


def menu_principal():
    """
    Muestra el menú y controla el programa.
    """
    restaurante = Restaurante()
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
            restaurante.insertar_elemento()
        elif opcion == "2":
            restaurante.buscar_elemento()
        elif opcion == "3":
            restaurante.modificar_elemento()
        elif opcion == "4":
            restaurante.eliminar_elemento()
        elif opcion == "5":
            restaurante.mostrar_todos()
        elif opcion == "6":
            print("Saliendo del programa...")
        else:
            print("Opción incorrecta.")


menu_principal()
