from persistencia.dao_generico import DAOGenerico
from entidade.doador import Doador

class DoadorDAO(DAOGenerico):
    def __init__(self):
        super().__init__('doadores.pkl')

    def adiciona(self, doador: Doador):
        if (isinstance(doador.cpf, int)) and (doador is not None) and isinstance(doador, Doador):
            super().adiciona(doador.cpf, doador)

    def pegar(self, cpf: int):
        if isinstance(cpf, int):
            return super().pegar(cpf)

    def remove(self, cpf: int):
        if isinstance(cpf, int):
            return super().remove(cpf)