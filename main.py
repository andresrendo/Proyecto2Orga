from RentAGame import RentAGame
import re

def validar_modelo(modelo, rent_a_game):
    # debe tener 6 letras y 2 numeros
    # el modelo debe ser unico (buscar por modelo, si no encuentra se crea, y si se encuentra, se muestra mensaje de error)
   
    patron = r"^[a-zA-Z]{6}\d{2}$"
    #verificacion del patron
    if re.match(patron, modelo):
        # patron aceptado, ahora ver si el modelo existe
        juego = rent_a_game.buscar_por_modelo(modelo)
        if juego:
            print("\033[0;31m \nEl modelo del juego ya existe\033[0m")
            return False
        else:
            return True
    else:
        print("\033[0;31m \nEl modelo debe contener 6 letras mayusculas, seguidas de 2 digitos\033[0m")
        return False

def validar_titulo(titulo, rent_a_game):
    
    # maximo 10 caracteres
    if len(titulo) <= 10:
        # el titulo tiene el tamaño correcto, ahora ver si el titulo existe
        juego = rent_a_game.buscar_por_titulo(titulo)
        if juego:
            print("\033[0;31m \nEl titulo del juego ya existe\033[0m")
            return False
        else:
            return True
    else:
        print("\033[0;31m \nEl titulo debe tener un maximo de 10 caracteres\033[0m")
        return False

def validar_precio(precio):
    # debe ser un numero entero
    # hasta 999, si tiene mas de 3 digitos, se muestra mensaje de error
    if precio.isdigit() and int(precio) != 0 and len(precio) <= 3:
        return True
    else:
        print("\033[0;31m \nEl precio debe ser un numero entero, distinto a 0, hasta 999\033[0m")
        return False

def mostrar_menu():
    print("""
            ¿Qué desea hacer?

        1. Insertar nuevo juego.
        2. Buscar juego por Modelo.
        3. Buscar juego por Título.
        4. Alquilar un juego.
        5. Devolver un juego.
        6. Eliminar juego.
        7. Salir.
""")

def main():
    rent_a_game = RentAGame()
    rent_a_game.cargar_base_de_datos()
    print("\nBase de datos cargada")

    print("""

        ╔═══╦═══╦═╗░╔╦════╗░░░░╔═══╗░░░░╔═══╦═══╦═╗╔═╦═══╗
        ║╔═╗║╔══╣║╚╗║║╔╗╔╗║░░░░║╔═╗║░░░░║╔═╗║╔═╗║║╚╝║║╔══╝
        ║╚═╝║╚══╣╔╗╚╝╠╝║║╚╝░░░░║║░║║░░░░║║░╚╣║░║║╔╗╔╗║╚══╗
        ║╔╗╔╣╔══╣║╚╗║║░║║░░╔══╗║╚═╝║╔══╗║║╔═╣╚═╝║║║║║║╔══╝
        ║║║╚╣╚══╣║░║║║░║║░░╚══╝║╔═╗║╚══╝║╚╩═║╔═╗║║║║║║╚══╗
        ╚╝╚═╩═══╩╝░╚═╝░╚╝░░░░░░╚╝░╚╝░░░░╚═══╩╝░╚╩╝╚╝╚╩═══╝
""")

    while True:
        mostrar_menu()
        opcion = input("            Seleccione la opcion de su preferencia: ")

        if opcion == "1":
            while True:
                modelo = input("\nIngrese el modelo: ")
                titulo = input("Ingrese el título: ")
                precio = input("Ingrese el precio: ")

                if validar_modelo(modelo, rent_a_game):
                    if validar_titulo(titulo, rent_a_game):
                        if validar_precio(precio):
                            rent_a_game.insertar_juego(modelo, titulo, precio)
                            print("\033[1;32m \nJuego insertado\033[0m")
                            break
                #        else:
                #            print("\033[0;31m \nPrecio inválido, por favor intente de nuevo.\033[0m")
                #    else:
                #        print("\033[0;31m \nTítulo inválido, por favor intente de nuevo.\033[0m")
                #else:
                #    print("\033[0;31m \nModelo inválido, por favor intente de nuevo.\033[0m")

        elif opcion == "2":
            modelo = input("\nIngrese el modelo: ")
            juego = rent_a_game.buscar_por_modelo(modelo)
            if juego:
                print(f"Título: {juego.titulo}")
                print(f"Precio: {juego.precio}")
                print(f"Status: {juego.status}")
            else:
                print("\033[0;31m Juego no encontrado\033[0m")

        elif opcion == "3":
            titulo = input("\nIngrese el título: ")
            juego = rent_a_game.buscar_por_titulo(titulo)
            if juego:
                print(f"Modelo: {juego.modelo}")
                print(f"Precio: {juego.precio}")
                print(f"Status: {juego.status}")
            else:
                print("Juego no encontrado")

        elif opcion == "4":
            modelo = input("\nIngrese el modelo: ")
            if rent_a_game.alquilar_juego(modelo):
                print("Juego alquilado")
            else:
                print("Juego no disponible para alquilar")

        elif opcion == "5":
            modelo = input("\nIngrese el modelo: ")
            if rent_a_game.devolver_juego(modelo):
                print("Juego devuelto")
            else:
                print("Juego no disponible para devolver")

        elif opcion == "6":
            modelo = input("\nIngrese el modelo: ")
            if rent_a_game.eliminar_juego(modelo):
                print("Juego eliminado")
            else:
                print("Juego no encontrado")

        elif opcion == "7":
            rent_a_game.guardar_base_de_datos()
            print("\033[1;37m \nGracias por usar RentAGame, los datos se han guardado en la base de datos.\n\033[0m")
            break

        else:
            print("\n\033[1;31m Ingreso inválido, por favor intente de nuevo.\033[0m")

main()