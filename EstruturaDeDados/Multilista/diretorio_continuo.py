class DiretorioContínuo:
    def __init__(self):
        self.__indices = []

    def indexar(self, elemento, campo):
        valor = getattr(elemento, campo)
        self.__indices.append((valor, elemento))
        self.__indices.sort(key=lambda x: x[0])  # Ordenar para facilitar buscas

    def consultar(self, min_val, max_val):
        return [e[1] for e in self.__indices if min_val <= e[0] <= max_val]

    def limpar(self):
        self.__indices = []