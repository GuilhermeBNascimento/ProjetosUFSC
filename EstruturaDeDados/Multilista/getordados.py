from diretorio_continuo import DiretorioContinuo
from diretorio_discreto import DiretorioDiscreto

class GestorDeDados:
    def __init__(self):
        self.elementos = {}  # chave: ID, valor: objeto Estudante
        self.diretorio_matricula = DiretorioDiscreto()
        self.diretorio_curso = DiretorioDiscreto()
        self.diretorio_time_torce = DiretorioDiscreto()
        self.diretorio_cidade_origem = DiretorioDiscreto()
        self.diretorio_valor_continuo = DiretorioContinuo()

    def inserir(self, elemento):
        self.elementos[elemento.id] = elemento
        self.diretorio_matricula.adicionar(elemento.matricula, elemento.id)
        self.diretorio_curso.adicionar(elemento.curso, elemento.id)
        self.diretorio_time_torce.adicionar(elemento.time_torce, elemento.id)
        self.diretorio_cidade_origem.adicionar(elemento.cidade_origem, elemento.id)

    def buscar_por_id(self, id):
        return self.elementos.get(id)

    def excluir_por_id(self, id):
        elemento = self.elementos.pop(id, None)
        if elemento:
            self.diretorio_matricula.dados[elemento.matricula].remove(id)
            self.diretorio_curso.dados[elemento.curso].remove(id)
            self.diretorio_time_torce.dados[elemento.time_torce].remove(id)
            self.diretorio_cidade_origem.dados[elemento.cidade_origem].remove(id)

    def exibir_dados(self):
        for elemento in self.elementos.values():
            print(vars(elemento))

    def consulta_simples(self, campo, valor):
        if campo == "matricula":
            return self.diretorio_matricula.consultar(valor)
        elif campo == "curso":
            return self.diretorio_curso.consultar(valor)
        elif campo == "time_torce":
            return self.diretorio_time_torce.consultar(valor)
        elif campo == "cidade_origem":
            return self.diretorio_cidade_origem.consultar(valor)
        return []

    def consulta_composta(self, campo1, valor1, campo2, valor2):
        resultado1 = self.consulta_simples(campo1, valor1)
        resultado2 = self.consulta_simples(campo2, valor2)
        return list(set(resultado1) & set(resultado2))
