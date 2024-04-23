from persistencia.dao_generico import DAOGenerico
from entidade.cachorro import Cachorro

class CachorroDAO(DAOGenerico):
    def __init__(self):
        super().__init__('cachorros.pkl')

    def adiciona(self, cachorro: Cachorro):
        if (isinstance(cachorro.numero_chip, str)) and (cachorro is not None) and isinstance(cachorro, Cachorro):
            super().adiciona(cachorro.numero_chip, cachorro)

    def pegar(self, numero_chip: str):
        if isinstance(numero_chip, str):
            return super().pegar(numero_chip)

    def remove(self, numero_chip: str):
        if isinstance(numero_chip, str):
            return super().remove(numero_chip)
