from modelos.nacionalidad import Nacionalidad


class Autor(Nacionalidad):
    def __init__(self, id_autor, nombre_autor, id_nacionalidad, pseudonimo, biografia):
        super().__init__(id_nacionalidad)  # type: ignore
        self.__id_autor = id_autor
        self.__nombre_autor = nombre_autor
        self.__pseudonimo = pseudonimo
        self.__biografia = biografia
