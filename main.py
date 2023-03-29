from RentAGame import RentAGame

def validar_modelo(modelo):
    # debe tener 6 letras y 2 numeros
    # el modelo debe ser unico (buscar por modelo, si no encuentra se crea, y si se encuentra, se muestra mensaje de error)
    pass

def validar_titulo(titulo):
    # maximo 10 caracteres
    # el titulo debe ser unico (buscar por titulo, si no encuentra se crea, y si se encuentra, se muestra mensaje de error)
    pass

def validar_precio(precio):
    # debe ser un numero entero
    # hasta 999, si tiene mas de 3 digitos, se muestra mensaje de error
    pass


def mostrar_menu():
    print("\n1. Insertar Juego")
    print("2. Buscar por Modelo")
    print("3. Buscar por Título")
    print("4. Alquilar Juego")
    print("5. Devolver Juego")
    print("6. Eliminar Juego")
    print("7. Guardar Base de Datos")
    print("8. Cargar Base de Datos")
    print("9. Salir")

def main():
    rent_a_game = RentAGame()

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
        opcion = input("Ingrese una opción: \n==> ")

        if opcion == "1":
            modelo = input("Ingrese el modelo: ")
            titulo = input("Ingrese el título: ")
            precio = int(input("Ingrese el precio: "))
            rent_a_game.insertar_juego(modelo, titulo, precio)

        elif opcion == "2":
            modelo = input("Ingrese el modelo: ")
            juego = rent_a_game.buscar_por_modelo(modelo)
            if juego:
                print(f"Título: {juego.titulo}")
                print(f"Precio: {juego.precio}")
                print(f"Status: {juego.status}")
            else:
                print("Juego no encontrado")

        elif opcion == "3":
            titulo = input("Ingrese el título: ")
            juego = rent_a_game.buscar_por_titulo(titulo)
            if juego:
                print(f"Modelo: {juego.modelo}")
                print(f"Precio: {juego.precio}")
                print(f"Status: {juego.status}")
            else:
                print("Juego no encontrado")

        elif opcion == "4":
            modelo = input("Ingrese el modelo: ")
            if rent_a_game.alquilar_juego(modelo):
                print("Juego alquilado")
            else:
                print("Juego no disponible para alquilar")

        elif opcion == "5":
            modelo = input("Ingrese el modelo: ")
            if rent_a_game.devolver_juego(modelo):
                print("Juego devuelto")
            else:
                print("Juego no disponible para devolver")

        elif opcion == "6":
            modelo = input("Ingrese el modelo: ")
            if rent_a_game.eliminar_juego(modelo):
                print("Juego eliminado")
            else:
                print("Juego no encontrado")

        elif opcion == "7":
            rent_a_game.guardar_base_de_datos()

        elif opcion == "8":
            rent_a_game.cargar_base_de_datos()
            print("Base de datos cargada")

        elif opcion == "9":
            break

        else:
            print("\n\033[1;31m Ingreso inválido, por favor intente de nuevo.\033[0m")

main()