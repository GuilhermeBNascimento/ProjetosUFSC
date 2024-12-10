class Multilista:
    def __init__(self):
        self.__elementos = {}

    def inserir(self, veiculo):
        if veiculo.identificador in self.__elementos:
            print("Erro: Identificador já existente.")
            return False
        self.__elementos[veiculo.identificador] = veiculo
        return True

    def buscar(self, identificador):
        return self.__elementos.get(identificador, None)

    def remover(self, identificador):
        return self.__elementos.pop(identificador, None)

    def listar_todos(self):
        return list(self.__elementos.values())
