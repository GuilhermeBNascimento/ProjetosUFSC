from persistencia.dao_generico import DAOGenerico
from entidade.adotante import Adotante

class AdotanteDAO(DAOGenerico):
    def __init__(self):
        super().__init__('adotantes.pkl')

    def adiciona(self, adotante: Adotante):
        if (isinstance(adotante.cpf, int)) and (adotante is not None) and isinstance(adotante, Adotante):
            super().adiciona(adotante.cpf, adotante)

    def pegar(self, cpf: int):
        if isinstance(cpf, int):
            return super().pegar(cpf)

    def remove(self, cpf: int):
        if isinstance(cpf, int):
            return super().remove(cpf)