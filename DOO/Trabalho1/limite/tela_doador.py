from limite.tela_abstrata import TelaAbstrata
from datetime import date


class TelaDoador(TelaAbstrata):
    def tela_opcoes(self):
        print("----- Registar Doador -----")
        print("Escolha sua opção: ")
        print("1 - Cadastrar Doador")
        print("2 - Editar Doador")
        print("3 - Remover Doador")
        print("4 - Listar Doador")
        print("5 - Procurar Doador")
        print("0 - Retornar")
        opcao = self.valida_inteiro("Escolha a opção:", [0, 1, 2, 3, 4, 5])
        return opcao

    def pega_dados_doador(self):
        print("----- DADOS DOADOR -----")
        nome = self.valida_num_strig("Nome Doador: ")
        cpf = self.valida_inteiro("CPF Doador: ")
        ano = self.valida_ano("Ano de Nascimento: ")
        mes = self.valida_mes("Mês de Nascimento: ")
        dia = self.valida_dia("Dia de Nascimento: ")
        data_nascimento = date(year=ano, month=mes, day=dia)
        endereco = input("Endereço Doador: ")
        telefone = self.valida_inteiro("Telefone Doador: ")

        return {"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento,
                "endereco": endereco, "telefone": telefone}

    def mostra_doador(self, dados_doador):
        print("DOADOR: ")
        print("NOME: ", dados_doador["nome"])
        print("CPF: ", dados_doador["cpf"])
        print("DATA DE NASCIMENTO: ", dados_doador["data_nascimento"])
        print("ENDEREÇO: ", dados_doador["endereco"])
        print("TELEFONE: ", dados_doador["telefone"])
        print("\n")

    def seleciona_doador(self):
        cpf_doador = self.valida_inteiro("CPF do doador que"
                                         " deseja selecionar: ")
        return cpf_doador

    def mostra_mensagem(self, msg):
        print(msg)
