from elemento import Elemento

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.__inicio = None
        self.__fim = None
        self.__cursor = None
        self.__elemento = Elemento

    def AcessarAtual(self):
        return self.__cursor.elemento.dado

    def InserirAntesAtual(self, novo):
        Novov = Elemento(novo)
        if self.__cursor is not None:
            Novov.ant = self.__cursor.ant
            Novov.prox = self.__cursor