from modelos.biblioteca import Biblioteca
from modelos.direccion import Direccion


class Lector(Biblioteca, Direccion):
    def __init__(self, id_lector, id_biblioteca, id_direccion, rut, digito_verificador, nombre_lector, correo_lector, habilitado):
        super().__init__(id_biblioteca)  # type: ignore
        super().__init__(id_direccion)  # type: ignore
        self.__id_lector = id_lector
        self.__rut = rut
        self.__digito_verificador = digito_verificador
        self.__nombre_lector = nombre_lector
        self.__correo_lector = correo_lector
        self.__habilitado = habilitado
