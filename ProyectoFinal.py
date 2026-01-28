
import logging;
import json;

"""
He creado un proyecto sobre un restaurante de la forma mas simple posible pero que nos
permite  añadir, buscar, modificar, eliminar y mostrar platos.
"""

"""
Configuracion del logging

"""
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Programa iniciado")

"""
Configuracion para los JSON
"""
def cargar_datos():


    try:
        with open("menu.json", "r") as archivo:
            return json.load(archivo)
    except:
        logging.warning("No se pudo cargar menu.json, se inicia menú vacío")
        return []

def guardar_datos(datos):
    """
    Guarda los datos del menú en un archivo JSON.
    """
    with open("menu.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

menu = cargar_datos()


def insertar_elemento(datos):
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

        datos.append(plato)
        guardar_datos(datos)

    logging.info(f"Plato añadido: {plato}")
        print("Plato añadido correctamente.")

except:
        logging.error("Error al insertar un plato")
        print("Error: datos incorrectos.")

def buscar_elemento(datos):
    """
    Busca un plato por su ID y lo muestra.

    """
    try:
        id_buscar = int(input("ID del plato a buscar: "))

        for plato in datos:
            if plato["id"] == id_buscar:
                print(plato)
            logging.info(f"Plato buscado: {plato}")
                return

        print("Plato no encontrado.")
            logging.info(f"Plato no encontrado al buscar ID {id_buscar}")
    except:
            logging.error("Error al buscar un plato")
        print("Error al buscar el plato.")


def modificar_elemento(datos):
    """
    Modifica el precio de un plato.
    """
    try:
        id_modificar = int(input("ID del plato a modificar: "))

        for plato in datos:
            if plato["id"] == id_modificar:
                nuevo_precio = float(input("Nuevo precio: "))
                plato["precio"] = nuevo_precio


            guardar_datos(datos)
                logging.info(f"Plato modificado: {plato}")



                print("Plato modificado.")
                return

        print("Plato no encontrado.")
         logging.info(f"No se encontró plato para modificar con ID {id_modificar}")

    except:
            logging.error("Error al modificar un plato")
        print("Error al modificar el plato.")


def eliminar_elemento(datos):
    """
    Elimina un plato del menú.

    """
    try:
        id_eliminar = int(input("ID del plato a eliminar: "))

        for plato in datos:
            if plato["id"] == id_eliminar:
                datos.remove(plato)


                guardar_datos(datos)
                logging.info(f"Plato eliminado: {plato}")


                print("Plato eliminado.")
                return

        print("Plato no encontrado.")
            logging.info(f"No se encontró plato para eliminar con ID {id_eliminar}")
    except:
        logging.error("Error al eliminar un plato")
        print("Error al eliminar el plato.")


def mostrar_todos(datos):
    """
    Muestra todos los platos del menú.

    """
    if datos == []:
        print("El menú está vacío.")
        logging.info("Se intentó mostrar el menú vacío")
    else:
        for plato in datos:
            print(plato)
            logging.info("Se mostró el menú completo")


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
            logging.info("Programa finalizado por el usuario")
            print("Saliendo del programa...")
        else:
            print("Opción incorrecta.")


menu_principal()
