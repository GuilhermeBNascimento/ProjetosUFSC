from datetime import date
from entidade.animal import Animal
from entidade.doador import Doador


class Doacao:
    def __init__(self, data_doacao: date, animal: Animal, doador: Doador,
                 motivo_doacao: str):
        self.__data_doacao = data_doacao
        self.__animal = animal
        self.__doador = doador
        self.__motivo_doacao = motivo_doacao

    @property
    def data_doacao(self):
        return self.__data_doacao

    @data_doacao.setter
    def data_doacao(self, data_doacao: date):
        if isinstance(data_doacao, date):
            self.__data_doacao = data_doacao

    @property
    def animal(self):
        return self.__animal

    @animal.setter
    def animal(self, animal: Animal):
        if isinstance(animal, Animal):
            self.__animal = animal

    @property
    def doador(self):
        return self.__doador

    @doador.setter
    def doador(self, doador: Doador):
        if isinstance(doador, Doador):
            self.__doador = doador

    @property
    def motivo_doacao(self):
        return self.__motivo_doacao

    @motivo_doacao.setter
    def motivo_doacao(self, motivo_doacao: str):
        if isinstance(motivo_doacao, str):
            self.__motivo_doacao = motivo_doacao
