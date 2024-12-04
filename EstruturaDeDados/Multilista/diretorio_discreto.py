class DiretorioDiscreto:
    def __init__(self):
        self.dados = {}  # chave: valor discreto, valor: lista de IDs de elementos

    def adicionar(self, valor, id_elemento):
        if valor not in self.dados:
            self.dados[valor] = []
        self.dados[valor].append(id_elemento)

    def consultar(self, valor):
        return self.dados.get(valor, [])
