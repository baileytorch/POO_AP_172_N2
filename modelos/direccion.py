from modelos.comuna import Comuna


class Direccion(Comuna):
    def __init__(self, id_direccion, id_comuna, calle, numero, departamento):
        super().__init__(id_direccion)  # type: ignore
        self.__id_comuna = id_comuna
        self.__calle = calle
        self.__numero = numero
        self.__departamento = departamento
