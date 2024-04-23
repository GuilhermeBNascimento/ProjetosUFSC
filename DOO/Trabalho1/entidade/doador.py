from entidade.pessoa import Pessoa
from datetime import date


class Doador(Pessoa):
    def __init__(self, nome: str, cpf: int, data_nascimento: date,
                 endereco: str, telefone: int):
        super().__init__(nome, cpf, data_nascimento, endereco)
        self.__telefone = telefone

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: int):
        if isinstance(telefone, int):
            self.__telefone = telefone
