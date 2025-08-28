# La clase es la PLANTILLA pra crear objetos del tipo de esa clase

class Nacionalidad():
    # función __init__ CONSTRUCTOR, se encargará de "construir" los objetos de esa clase
    # en base a la PLANTILLA definida
    def __init__(self, id_nacionalidad, pais, nacionalidad):
        # Los atributos del objeto SELF son PRIVADOS, estan ENCAPSULADOS dentro del constructor
        self.__id_nacionalidad = id_nacionalidad
        self.__pais = pais
        self.__nacionalidad = nacionalidad
