class DiretorioDiscreto:
    def __init__(self):
        self.__indices = {}

    def indexar(self, elemento, campo):
        valor = getattr(elemento, campo)
        if valor not in self.__indices:
            self.__indices[valor] = []
        self.__indices[valor].append(elemento)

    def consultar(self, valor):
        return self.__indices.get(valor, [])

    def limpar(self):
        self.__indices = {}

