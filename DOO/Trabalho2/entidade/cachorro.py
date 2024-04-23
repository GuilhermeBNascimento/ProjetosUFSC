from entidade.animal import Animal


class Cachorro(Animal):
    def __init__(self, numero_chip: str, nome: str, raca: str, tamanho: str):
        super().__init__(numero_chip, nome, raca)
        self.__tamanho = tamanho
        self.__vacinas = []

    @property
    def tamanho(self):
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, tamanho: str):
        if isinstance(tamanho, str):
            self.__tamanho = tamanho

    @property
    def vacinas(self):
        return self.__vacinas