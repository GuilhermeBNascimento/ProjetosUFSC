class Multilista:
    def __init__(self):
        self.elementos = {}

    def inserir(self, veiculo):
        if veiculo.identificador in self.elementos:
            print("Erro: Identificador já existente.")
            return False
        self.elementos[veiculo.identificador] = veiculo
        return True

    def buscar(self, identificador):
        return self.elementos.get(identificador, None)

    def remover(self, identificador):
        return self.elementos.pop(identificador, None)

    def listar_todos(self):
        return list(self.elementos.values())
