from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, numero_chip: str, nome: str, raca: str):
        self.__numero_chip = numero_chip
        self.__nome = nome
        self.__raca = raca

    @property
    def numero_chip(self):
        return self.__numero_chip

    @numero_chip.setter
    def numero_chip(self, numero_chip: str):
        if isinstance(numero_chip, str):
            self.__numero_chip = numero_chip

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, raca: str):
        if isinstance(raca, str):
            self.__raca = raca