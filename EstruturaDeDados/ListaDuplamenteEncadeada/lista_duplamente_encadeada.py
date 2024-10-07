from elemento import Elemento

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.__inicio = None
        self.__fim = None
        self.__cursor = None

    def AcessarAtual(self):
        return self.__cursor.valor

    def InserirAntesAtual(self, novo):
        Novov = Elemento(novo)
        if self.__cursor == None:
            Novov.ant = self.__cursor.ant
            Novov.prox = self.__cursor

        if self.__cursor.ant:
            self.__cursor.ant.prox = novo
        else:
            self.__inicio = novo
        self.__cursor.ant = novo

    def InserirAposAtual(self, novo):
        Novov = Elemento(novo)
        if self.__cursor is None:
            Novov.prox = self.__cursor.prox
            Novov.ant = self.__cursor

        if self.__cursor.prox:
            self.__cursor.prox.ant = novo
        else:
            self.__fim = novo
        self.__cursor.prox = novo

    def InserirComoUltimo(self, novo):
        Novov = Elemento(novo)
        if self.__fim:
            self.__fim.prox = novo
            Novov.ant = self.__fim
            self.__fim = novo
        else:
            self.__inicio = novo
            self.__fim = novo
        self.__cursor = novo

    def InserirComoPrimeiro(self, novo):
        Novov = Elemento(novo)
        if self.__inicio:
            Novov.prox = self.__inicio
            self.__inicio.ant = novo
            self.__inicio = novo
        else:
            self.__inicio = novo
            self.__fim = novo
        self.__cursor = novo

    def InserirNaPosicao(self, k, novo):
        Novov = Elemento(novo)
        if k == 0:
            self.InserirComoPrimeiro(novo)
        atual = self.__inicio
        pos = 0

        while atual and pos < k:
            atual = atual.elemento.prox
            pos+=1

        if atual == None:
            self.InserirComoUltimo(novo)
        else:
            Novov.ant = atual.ant
            Novov.prox = atual
            if atual.ant:
                atual.ant.prox = novo
            atual.ant = novo

            if Novov.ant == None:
                self.__inicio = novo

    def ExcluirAtual(self):
        if self.__cursor == None:
            if self.__cursor.ant:
                self.__cursor.ant.prox = self.__cursor.prox
            else:
                self.__inicio = self.__cursor.prox
            if self.__cursor.prox:
                self.__cursor.prox.ant = self.__cursor.ant
            else:
                self.__fim = self.__cursor.ant
            self.__cursor = self.__cursor.prox

    def ExcluirPrimeiro(self):
        if self.__inicio == None:
            self.__cursor = self.__inicio
            self.ExcluirAtual()

    def ExcluirUltimo(self):
        if self.__fim == None:
            self.__cursor = self.__fim
            self.ExcluirAtual()

    def ExcluirElemento(self, chave):
        atual = self.__inicio
        while atual:
            if atual.elemento.valor == chave:
                self.__cursor = atual
                self.ExcluirAtual()
                atual = atual.elemento.prox

    def ExcluirDaPosicao(self, k):
        atual = self.__inicio
        pos = 0

        while atual and pos < k:
            atual = atual.prox
            pos+=1
        if atual:
            self.__cursor = atual
            self.ExcluirAtual()

    def Buscar(self, chave):
        atual = self.__inicio
        while atual:
            if atual.valor == chave:
                return True
            atual = atual.prox
        return False

    def AvancarKPosicoes(self, k):
        for _ in range(k):
            if self.__cursor and self.__cursor.prox:
                self.__cursor = self.__cursor.prox
            else:
                break  # Chegou ao final da lista

    def RetrocederKposicoes(self, k):
        for _ in range(k):
            if self.__cursor and self.__cursor.ant:
                self.__cursor = self.__cursor.ant
            else:
                break  # Chegou ao início da lista

    def irParaPrimeiro(self):
        self.__cursor = self.__inicio

    def irParaUltimo(self):
        self.__cursor = self.__fim