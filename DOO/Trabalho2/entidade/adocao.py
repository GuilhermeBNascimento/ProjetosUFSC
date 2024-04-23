from datetime import date
from entidade.animal import Animal
from entidade.adotante import Adotante


class Adocao:
    def __init__(self, codigo_adoao: int, data: date, animal: Animal, adotante: Adotante,
                 termo_responsabilidade: str):
        self.__data = data
        self.__animal = animal
        self.__adotante = adotante
        self.termo_responsabilidade = termo_responsabilidade
        self.__codigo_adocao = codigo_adoao

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: date):
        if isinstance(data, date):
            self.__data = data

    @property
    def animal(self):
        return self.__animal

    @animal.setter
    def animal(self, animal: Animal):
        if isinstance(animal, Animal):
            self.__animal = animal

    @property
    def adotante(self):
        return self.__adotante

    @adotante.setter
    def adotante(self, adotante: Adotante):
        if isinstance(adotante, Adotante):
            self.__adotante = adotante

    @property
    def termo_responsabilidade(self):
        return self.__termo_responsabilidade

    @termo_responsabilidade.setter
    def termo_responsabilidade(self, termo_responsabilidade: str):
        if isinstance(termo_responsabilidade, str):
            self.__termo_responsabilidade = termo_responsabilidade

    @property
    def codigo_adocao(self):
        return self.__codigo_adocao

    @codigo_adocao.setter
    def codigo_adocao(self, codigo_adocao: int):
        if isinstance(codigo_adocao, int):
            self.__codigo_adocao = codigo_adocao