from RentAGame import RentAGame










def mostrar_menu():
    print("1. Insertar Juego")
    print("2. Buscar por Modelo")
    print("3. Buscar por Título")
    print("4. Alquilar Juego")
    print("5. Devolver Juego")
    print("6. Eliminar Juego")
    print("7. Guardar Base de Datos")
    print("8. Cargar Base de Datos")
    print("9. Salir")

rent_a_game = RentAGame()

while True:
    mostrar_menu()
    opcion = input("Ingrese una opción: \n==>")
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
        filename = input("Ingrese el nombre del archivo: ")
        rent_a_game.guardar_base_de_datos(filename)
    elif opcion == "8":
        filename = input("Ingrese el nombre del archivo: ")
        rent_a_game.cargar_base_de_datos(filename)
    elif opcion == "9":
        break
    else:
        print("Opción inválida")
