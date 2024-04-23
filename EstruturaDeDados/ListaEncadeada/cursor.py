class Cursor:
    def __init__(self):
        self.__atual = None

    @property
    def atual(self):
        return self.__atual

    @atual.setter
    def atual(self, atual):
        self.__atual = atual

    def irParaPrimeiro(self):
        while self.__atual.ant is not None:
            self.__atual = self.__atual.ant

    def irParaUltimo(self):
        while self.__atual.prox is not None:
            self.__atual = self.__atual.prox

    def avancarKPosicoes(self, k):
        for i in range(k):
            self.__atual = self.__atual.prox

    def retocederKPosicoes(self, k):
        for i in range(k):
            self.__atual = self.__atual.ant