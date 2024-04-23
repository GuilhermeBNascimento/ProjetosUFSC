from datetime import date


class Vacina:
    def __init__(self, nome_vacina: str, data_vacina: date):
        self.__nome_vacina = nome_vacina
        self.__data_vacina = data_vacina

    @property
    def nome_vacina(self):
        return self.__nome_vacina

    @property
    def data_vacina(self):
        return self.__data_vacina