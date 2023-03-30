import pickle


# __init__(self): este método se utiliza para inicializar la clase. En este caso, se inicializan los grupos primarios, los grupos de overflow y el índice de título.

# hash_func(self, modelo): este método utiliza una función de hash para calcular el índice en el que se debe almacenar el juego en la tabla hash.

# insertar_juego(self, modelo, titulo, precio): este método se utiliza para insertar un nuevo juego en la base de datos. Crea un nuevo objeto Juego con los parámetros especificados, calcula su índice hash y lo agrega a la tabla hash o al grupo de overflow si la tabla hash está llena. También actualiza el índice de título.

# buscar_por_modelo(self, modelo): este método se utiliza para buscar un juego por su modelo en la base de datos. Calcula su índice hash y busca en la tabla hash y en los grupos de overflow hasta que encuentra el juego o llega al final sin encontrarlo. Devuelve el juego encontrado o None si no se encuentra.

# buscar_por_titulo(self, titulo): este método se utiliza para buscar un juego por su título en el índice de título. Devuelve el juego encontrado o None si no se encuentra.

# alquilar_juego(self, modelo): este método se utiliza para marcar un juego como alquilado en la base de datos. Busca el juego por su modelo y, si se encuentra y su estado es "EN STOCK", lo marca como "ALQUILADO" y devuelve True. De lo contrario, devuelve False.

# devolver_juego(self, modelo): este método se utiliza para marcar un juego como devuelto en la base de datos. Busca el juego por su modelo y, si se encuentra y su estado es "ALQUILADO", lo marca como "EN STOCK" y devuelve True. De lo contrario, devuelve False.

# eliminar_juego(self, modelo): este método se utiliza para eliminar un juego de la base de datos. Busca el juego por su modelo y, si se encuentra, lo elimina de la tabla hash o del grupo de overflow y lo elimina del índice de título. Devuelve True si el juego se elimina correctamente y False si no se encuentra.

# guardar_base_de_datos(self, filename): este método se utiliza para guardar los datos de la base de datos en un archivo de secuencia de bytes en el disco duro. Crea un diccionario con los datos de la tabla hash, los grupos de overflow y el índice de título y los guarda en un archivo "base_datos".

# cargar_base_de_datos(self, filename): este método se utiliza para cargar los datos de la base de datos desde un archivo de secuencia de bytes en el disco duro. Abre el archivo "base_datos", y carga los datos en un diccionario




class Juego:
    def __init__(self, modelo, titulo, precio, status):
        self.modelo = modelo
        self.titulo = titulo
        self.precio = precio
        self.status = status

class RentAGame:
    def __init__(self):
        self.capacidad = 3
        self.tabla = [[], [], []] # 3 grupos primarios
        self.overflow = [[], [], [], [], [], []] # 6 grupos de overflow
        self.indice_titulo = {}

    def hash_func(self, modelo):
        return sum([ord(c) for c in modelo]) % 3

    def insertar_juego(self, modelo, titulo, precio):

        juego = Juego(modelo, titulo.upper(), precio, "EN STOCK")
        index = self.hash_func(modelo)

        if len(self.tabla[index]) < self.capacidad:
            self.tabla[index].append(juego)
        else:
            for i in range(len(self.overflow)):
                if len(self.overflow[i]) < self.capacidad:
                    self.overflow[i].append(juego)
                    break
        self.indice_titulo[titulo.upper()] = juego.modelo

    def buscar_por_modelo(self, modelo):

        index = self.hash_func(modelo.upper())

        for juego in self.tabla[index]:
            if juego.modelo == modelo.upper():
                return juego
        for lista in self.overflow:
            for juego in lista:
                if juego.modelo == modelo.upper():
                    return juego
        return None

    def buscar_por_titulo(self, titulo):
        # clave primaria del juego obtenida con el indice
        modelo_juego = self.indice_titulo.get(titulo.upper())
        if modelo_juego:
            return self.buscar_por_modelo(modelo_juego)
        else:
            return None

    def alquilar_juego(self, modelo):

        juego = self.buscar_por_modelo(modelo)
        if juego and juego.status == "EN STOCK":
            juego.status = "ALQUILADO"
            return True
        else:
            return False

    def devolver_juego(self, modelo):

        juego = self.buscar_por_modelo(modelo)
        if juego and juego.status == "ALQUILADO":
            juego.status = "EN STOCK"
            return True
        else:
            return False

    def eliminar_juego(self, modelo):

        index = self.hash_func(modelo)
        for i, juego in enumerate(self.tabla[index]):
            if juego.modelo == modelo:
                self.tabla[index].pop(i)
                del self.indice_titulo[juego.titulo]
                return True

        for lista in self.overflow:
            for i, juego in enumerate(lista):
                if juego.modelo == modelo:
                    lista.pop(i)
                    del self.indice_titulo[juego.titulo]
                    return True
        return False

    def guardar_base_de_datos(self):

        data = {
            "tabla": self.tabla,
            "overflow": self.overflow,
            "indice_titulo": self.indice_titulo
        }
        with open("base_datos", "wb") as f:
            pickle.dump(data, f)

    def cargar_base_de_datos(self):
        
        with open("base_datos", "rb") as f:
            data = pickle.load(f)

        self.tabla = data["tabla"]
        self.overflow = data["overflow"]
        self.indice_titulo = data["indice_titulo"]

