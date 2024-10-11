class NO:
    def __init__(self, valor):
        self.__valor = valor
        self.__anterior = None
        self.__proximo = None

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
         self.__valor = valor

    @property
    def anterior(self):
        return self.__anterior

    @anterior.setter
    def anterior(self, anterior):
        self.__anterior = anterior

    @property
    def proximo(self):
        return self.__proximo

    @proximo.setter
    def proximo(self, proximo):
        self.__proximo = proximo