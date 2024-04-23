from limite.tela_abstrata import TelaAbstrata
from datetime import date


class TelaAdocao(TelaAbstrata):
    def tela_opcoes(self):
        print("----- Registar Adocao -----")
        print("Escolha sua opção: ")
        print("1 - Cadastrar Adoção")
        print("2 - Editar Adoção")
        print("3 - Remover Adoção")
        print("4 - Listar Adoções")
        print("5 - Procurar Adoção")
        print("6 - Relatório de Adoçôes por data")
        print("0 - Retornar")
        opcao = self.valida_inteiro("Escolha a opção:", [0, 1, 2, 3, 4, 5, 6])
        return opcao

    def pega_dados_adocao(self):
        print("----- DADOS ADOÇÃO -----")
        ano = self.valida_ano("Ano da Adoação: ")
        mes = self.valida_mes("Mês da Adoação: ")
        dia = self.valida_dia("Dia da Adoação: ")
        data_adoacao = date(year=ano, month=mes, day=dia)
        animal_adotado = self.valida_animal("O Animal Adoado é "
                                            "um Gato ou Cachorro? ")
        numero_chip = self.valida_inteiro("Número do chip do Animal (Sem o 'C'"
                                          " ou 'G' na frente): ")
        numero_chip = self.\
            transforma_string_adiciona_caracter_frente(animal_adotado,
                                                       numero_chip)
        cpf = self.valida_inteiro("CPF do adotante: ")
        termo_responsabilidade = self.termo_responsabilidade("Você assina esse"
                                                             " termo?: SIM "
                                                             "ou NAO ")

        return {"data_adocao": data_adoacao, "numero_chip": numero_chip,
                "cpf": cpf, "animal_adotado": animal_adotado,
                "termo_responsabilidade": termo_responsabilidade}

    def mostra_adocao(self, dados_adocao):
        print("ADOÇÃO: ")
        print("DATA DA ADOÇÃO: ", dados_adocao["data_adocao"])
        print("TERMO DE RESPONSABILIDADE: ", dados_adocao
              ["termo_responsabilidade"])
        print("\n")

    def seleciona_adocao(self):
        cpf_adotante = self.valida_inteiro("CPF do adotante da adoção "
                                           "que deseja selecionar: ")
        return cpf_adotante

    def mostra_mensagem(self, msg):
        print(msg)

    def pega_data_relatorio(self):
        while True:
            print("Data inicial do relatório: ")
            ano = self.valida_ano("Ano do começo dos dados do relatório: ")
            mes = self.valida_mes("Mês do começo dos dados do relatório: ")
            dia = self.valida_dia("Dia do começo dos dados do relatório: ")
            data_inicial = date(year=ano, month=mes, day=dia)
            print("Data final do relatório")
            ano = self.valida_ano("Ano do final dos dados do relatório: ")
            mes = self.valida_mes("Mês do final dos dados do relatório: ")
            dia = self.valida_dia("Dia do final dos dados do relatório: ")
            data_final = date(year=ano, month=mes, day=dia)
            try:
                if data_final > data_inicial:
                    return data_inicial, data_final
                else:
                    raise ValueError
            except ValueError:
                print("Data final dos dados, anterior a data inicial, "
                      "impossível de se criar relatório")

    def termo_responsabilidade(self, mensagem=""):
        while True:
            resposta_lida = input(mensagem)
            respostas_possiveis = ["SIM", "NAO"]
            try:
                resposta_lida = resposta_lida.upper()
                if resposta_lida not in respostas_possiveis:
                    raise ValueError
                if resposta_lida == "SIM":
                    return resposta_lida
                else:
                    print("Para concluir a adoção você precisa "
                          "assinar esse termo")
            except ValueError:
                print("Resposta incorreta!. Respostas Possíveis: SIM ou NÃO")
