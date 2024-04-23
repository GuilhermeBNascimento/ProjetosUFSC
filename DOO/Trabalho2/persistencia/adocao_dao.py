from entidade.adocao import Adocao
from persistencia.dao_generico import DAOGenerico

class AdocaoDAO(DAOGenerico):
    def __init__(self):
        super().__init__('adocoes.pkl')

    def adiciona(self, adocao: Adocao):
        if (isinstance(adocao.adotante.cpf, int)) and (adocao is not None) and isinstance(adocao, Adocao):
            super().adiciona(adocao.adotante.cpf, adocao)

    def pegar(self, cpf: int):
        if isinstance(cpf, int):
            return super().pegar(cpf)

    def remove(self, cpf: int):
        if isinstance(cpf, int):
            return super().remove(cpf)