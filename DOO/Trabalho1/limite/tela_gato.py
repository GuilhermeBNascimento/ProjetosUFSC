from limite.tela_abstrata import TelaAbstrata


class TelaGato(TelaAbstrata):

    def tela_opcoes(self):
        print("----- Registar Gato -----")
        print("Escolha sua opção: ")
        print("1 - Cadastrar Gato")
        print("2 - Editar Gato")
        print("3 - Remover Gato")
        print("4 - Listar Gato")
        print("5 - Procurar Gato")
        print("6 - Vacinas")
        print("7 - Listar Gatos Disponiveis")
        print("0 - Retornar")
        opcao = self.valida_inteiro("Escolha a opção:",
                                    [0, 1, 2, 3, 4, 5, 6, 7])
        return opcao

    def pega_dados_gato(self):
        print("----- DADOS GATO -----")
        numero_chip = self.valida_inteiro("Numero do Chip: ")
        numero_chip = \
            self.transforma_string_adiciona_caracter_frente("G", numero_chip)
        nome = self.valida_num_strig("Nome: ")
        raca = self.valida_num_strig("Raça: ")
        cor_pelo = self.valida_num_strig("Cor do Pelo do Gato: ")

        return {"numero_chip": numero_chip, "nome": nome,
                "raca": raca, "cor_pelo": cor_pelo}

    def mostra_gato(self, dados_gato):
        print("GATO:")
        print("NÚMERO DO CHIP: ", dados_gato["numero_chip"])
        print("NOME: ", dados_gato["nome"])
        print("RAÇA: ", dados_gato["raca"])
        print("COR DO PELO: ", dados_gato["cor_pelo"])
        print("\n")

    def seleciona_gato(self):
        numero_chip = self.valida_inteiro("Nùmero do chip do gato que deseja"
                                          " selecionar (sem o G na frente): ")
        numero_chip = \
            self.transforma_string_adiciona_caracter_frente("G", numero_chip)
        return numero_chip

    def mostra_mensagem(self, msg):
        print(msg)
