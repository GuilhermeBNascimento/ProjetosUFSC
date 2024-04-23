from limite.tela_abstrata import TelaAbstrata
from datetime import date


class TelaDoacao(TelaAbstrata):
    def tela_opcoes(self):
        print("----- Registar Doacao -----")
        print("Escolha sua opção: ")
        print("1 - Cadastrar Doação")
        print("2 - Editar Doação")
        print("3 - Remover Doação")
        print("4 - Listar Doações")
        print("5 - Procurar Doação")
        print("6 - Relatório de Doações por data")
        print("0 - Retornar")
        opcao = self.valida_inteiro("Escolha a opção:", [0, 1, 2, 3, 4, 5, 6])
        return opcao

    def pega_dados_doacao(self):
        print("----- DADOS DOAÇÃO -----")
        ano = self.valida_ano("Ano da Doação: ")
        mes = self.valida_mes("Mês da Doação: ")
        dia = self.valida_dia("Dia da Doação: ")
        data_doacao = date(year=ano, month=mes, day=dia)
        animal_doado = self.valida_animal("O Animal Doado é um"
                                          " Gato ou Cachorro? ")
        numero_chip = self.valida_inteiro("Número do chip do Animal "
                                          "(Sem o 'C' ou 'G' na frente): ")
        numero_chip = \
            self.transforma_string_adiciona_caracter_frente(animal_doado,
                                                            numero_chip)
        cpf = self.valida_inteiro("CPF do Doador: ")
        motivo_doacao = input("Motivo da Doação do Animal: ")

        return {"data_doacao": data_doacao, "numero_chip": numero_chip,
                "animal_doado": animal_doado, "cpf": cpf,
                "motivo_doacao": motivo_doacao}

    def mostra_doacao(self, dados_doacao):
        print("DATA DA DOAÇÃO: ", dados_doacao["data_doacao"])
        print("MOTIVO DA DOAÇÃO: ", dados_doacao["motivo_doacao"])

    def seleciona_doacao(self):
        cpf_doador = self.valida_inteiro("CPF do doador da doação"
                                         " que deseja selecionar: ")
        return cpf_doador

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

    def mostra_mensagem(self, msg):
        print(msg)

    def valida_animal(self, mensagem=" "):
        while True:
            tipo_animal_lido = input(mensagem)
            tipos_animais_possiveis = ["GATO", "CACHORRO"]
            try:
                tipo_animal_lido = tipo_animal_lido.upper()
                if tipo_animal_lido not in tipos_animais_possiveis:
                    raise ValueError
                if tipo_animal_lido == "GATO":
                    tipo_animal_lido = "G"
                    return tipo_animal_lido
                else:
                    tipo_animal_lido = "C"
                    return tipo_animal_lido
            except ValueError:
                print("Tipo de animal não aceito! Tipos de animais possíveis,"
                      " gato e cachorro!")
