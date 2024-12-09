class DiretorioDiscreto:
    def __init__(self):
        self.index = {}

    def inserir(self, dado, chave):
        """Insere um dado no índice discreto, baseado em uma chave (ex: cidade ou profissão)."""
        if chave not in self.index:
            self.index[chave] = []
        self.index[chave].append(dado)

    def remover(self, dado, chave):
        """Remove um dado do índice discreto."""
        if chave in self.index:
            self.index[chave].remove(dado)
            if not self.index[chave]:
                del self.index[chave]
        else:
            print(f"Erro: Chave {chave} não encontrada.")

    def buscar(self, chave):
        """Busca todos os dados que correspondem à chave discreta."""
        return self.index.get(chave, [])
