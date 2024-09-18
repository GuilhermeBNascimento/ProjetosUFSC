class Fila:
    def __init__(self, max):
        self.__max = max
        self.__dados = [None]*max
        self.__inicio = 0
        self.__fim = -1
        self.__qtdd = 0

    def entrar(self, novo):
        if self.__qtdd < self.__max:
            self.__fim = (self.__fim + 1) % self.__max
            self.__dados[self.__fim] = novo
            self.__qtdd += 1
        else:
            print("EXECEÇÂO!!!  Fila cheia, valor " , novo, "não inserido.")

    def sair(self):
        if self.__qtdd > 0:
            self.__qtdd-=1
            ret = self.__dados[self.__inicio]
            self.__dados[self.__inicio] = None
            self.__inicio += 1
        if self.__inicio == self.__max:
            self.__inicio = 0
            return ret
        else:
            print("EXCEÇÂO")

    def exibir(self):
        print(self.__dados)
        print(self.__qtdd)


a = Fila(3)
a.entrar(10)
a.entrar(15)
a.entrar(45)
a.entrar(50)
a.exibir()

