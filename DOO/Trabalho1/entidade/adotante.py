from entidade.pessoa import Pessoa
from datetime import date


class Adotante(Pessoa):
    def __init__(self, nome: str, cpf: int, data_nascimento: date,
                 endereco: str, tipo_habitacao: str, tamanho_residencia: str,
                 possui_animal: str):
        super().__init__(nome, cpf, data_nascimento, endereco)
        self.__tipo_habitacao = tipo_habitacao
        self.__tamanho_residencia = tamanho_residencia
        self.__possui_animal = possui_animal

    @property
    def tipo_habitacao(self):
        return self.__tipo_habitacao

    @tipo_habitacao.setter
    def tipo_habitacao(self, tipo_habitacao: str):
        if isinstance(tipo_habitacao, str):
            self.__tipo_habitacao = tipo_habitacao

    @property
    def tamanho_residencia(self):
        return self.__tamanho_residencia

    @tamanho_residencia.setter
    def tamanho_residencia(self, tamanho_residencia: str):
        if isinstance(tamanho_residencia, str):
            self.__tamanho_residencia = tamanho_residencia

    @property
    def possui_animal(self):
        return self.__possui_animal

    @possui_animal.setter
    def possui_animal(self, possui_animal: str):
        if isinstance(possui_animal, str):
            self.__possui_animal = possui_animal
