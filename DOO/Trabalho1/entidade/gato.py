from entidade.animal import Animal


class Gato(Animal):
    def __init__(self, numero_chip: int, nome: str, raca: str, cor_pelo: str):
        super().__init__(numero_chip, nome, raca)
        self.__cor_pelo = cor_pelo
        self.__vacinas = []

    @property
    def cor_pelo(self):
        return self.__cor_pelo

    @cor_pelo.setter
    def cor_pelo(self, cor_pelo: str):
        if isinstance(cor_pelo, str):
            self.__cor_pelo = cor_pelo

    @property
    def vacinas(self):
        return self.__vacinas
