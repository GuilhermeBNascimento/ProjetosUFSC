class DiretorioContínuo:
    def __init__(self):
        self.indices = []

    def indexar(self, elemento, campo):
        valor = getattr(elemento, campo)
        self.indices.append((valor, elemento))
        self.indices.sort(key=lambda x: x[0])  # Ordenar para facilitar buscas

    def consultar(self, min_val, max_val):
        return [e[1] for e in self.indices if min_val <= e[0] <= max_val]

    def limpar(self):
        self.indices = []