class DiretorioDiscreto:
    def __init__(self):
        self.indices = {}

    def indexar(self, elemento, campo):
        valor = getattr(elemento, campo)
        if valor not in self.indices:
            self.indices[valor] = []
        self.indices[valor].append(elemento)

    def consultar(self, valor):
        return self.indices.get(valor, [])

    def limpar(self):
        self.indices = {}

