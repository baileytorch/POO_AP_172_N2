from modelos.direccion import Direccion


class Biblioteca(Direccion):
    def __init__(self, id_biblioteca, id_direccion, nombre_biblioteca, web, habilitado):
        super().__init__(id_direccion)  # type: ignore
        self.__id_biblioteca = id_biblioteca
        self.__nombre_biblioteca = nombre_biblioteca
        self.__web = web
        self.__habilitado = habilitado
