from entidade.doacao import Doacao
from persistencia.dao_generico import DAOGenerico

class DoacaoDAO(DAOGenerico):
    def __init__(self):
        super().__init__('doacoes.pkl')

    def adiciona(self, doacao: Doacao):
        if (isinstance(doacao.doador.cpf, int)) and (doacao is not None) and isinstance(doacao, Doacaocao):
            super().adiciona(doacao.doador.cpf, doacao)

    def pegar(self, cpf: int):
        if isinstance(cpf, int):
            return super().pegar(cpf)

    def remove(self, cpf: int):
        if isinstance(cpf, int):
            return super().remove(cpf)