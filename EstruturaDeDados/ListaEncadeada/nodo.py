class Nodo:
    def __init__(self, valor = 0, ant = None, Prox = None):
        self.__valor = valor
        self.__ant = ant
        self.__prox = Prox

    
    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def ant(self):
        return self.__ant

    @ant.setter
    def ant(self, ant):
        self.__ant = ant

    @property
    def prox(self):
        return self.__prox

    @prox.setter
    def prox(self, prox):
        self.__prox = prox