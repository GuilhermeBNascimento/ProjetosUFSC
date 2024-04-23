from limite.tela_abstrata import TelaAbstrata
from datetime import date


class TelaVacina(TelaAbstrata):

    def tela_opcoes(self):
        print("----- Registar Vacina -----")
        print("Escolha sua opção: ")
        print("1 - Cadastrar Vacina no Animal Escolhido")
        print("2 - Editar Vacinas no Animal Escolhido")
        print("3 - Remover Vacinas no Animal Escolhido")
        print("4 - Listar Vacinas Aplicadas no Animal Escolhido")
        print("0 - Retornar")
        opcao = self.valida_inteiro("Escolha a opção:", [0, 1, 2, 3, 4])
        return opcao

    def pega_dados_vacina(self):
        print("----- DADOS VACINA -----")
        nome_vacina = self.valida_num_strig("Nome da Vacina: ")
        ano = self.valida_ano("Ano da Aplicação da Vacina: ")
        mes = self.valida_mes("Mês da Aplicação da Vacina: ")
        dia = self.valida_dia("Dia da Aplicação da Vacina: ")
        data_vacina = date(year=ano, month=mes, day=dia)

        return {"nome_vacina": nome_vacina, "data_vacina": data_vacina}

    def mostra_vacina(self, dados_vacina):
        print("VACINA:")
        print("NOME DA VACINA: ", dados_vacina["nome_vacina"])
        print("DATA DA VACINA: ", dados_vacina["data_vacina"])
        print("\n")

    def seleciona_vacina(self):
        nome_vacina = self.valida_num_strig("Nome da vacina que desejo "
                                            "selecionar: ")
        return nome_vacina

    def mostra_mensagem(self, msg):
        print(msg)
