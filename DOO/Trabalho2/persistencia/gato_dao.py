from persistencia.dao_generico import DAOGenerico
from entidade.gato import Gato

class GatoDAO(DAOGenerico):
    def __init__(self):
        super().__init__('gatos.pkl')

    def adiciona(self, gato: Gato):
        if (isinstance(gato.numero_chip, str)) and (gato is not None) and isinstance(gato, Gato):
            super().adiciona(gato.numero_chip, gato)

    def pegar(self, numero_chip: str):
        if isinstance(numero_chip, str):
            return super().pegar(numero_chip)

    def remove(self, numero_chip: str):
        if isinstance(numero_chip, str):
            return super().remove(numero_chip)