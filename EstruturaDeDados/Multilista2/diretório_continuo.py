class DiretorioContinuo:
    def __init__(self):
        self.index = {}

    def inserir(self, dado, faixa):
        """Insere um dado no índice contínuo, baseado em uma faixa (ex: faixa salarial)."""
        if faixa not in self.index:
            self.index[faixa] = []
        self.index[faixa].append(dado)

    def remover(self, dado, faixa):
        """Remove um dado do índice contínuo."""
        if faixa in self.index:
            self.index[faixa].remove(dado)
            if not self.index[faixa]:
                del self.index[faixa]
        else:
            print(f"Erro: Faixa {faixa} não encontrada.")

    def buscar(self, faixa):
        """Busca todos os dados em uma faixa contínua."""
        return self.index.get(faixa, [])

