from limite.tela_abstrata import TelaAbstrata


class TelaCachorro(TelaAbstrata):
    def tela_opcoes(self):
        print("----- Registar Cachorro -----")
        print("Escolha sua opção: ")
        print("1 - Cadastrar Cachorro")
        print("2 - Editar Cachorro")
        print("3 - Remover Cachorro")
        print("4 - Listar Cachorros")
        print("5 - Procurar Cachorro")
        print("6 - Vacinas")
        print("7 - Listar Cachorros Disponíveis")
        print("0 - Retornar")
        opcao = self.valida_inteiro("Escolha a opção:",
                                    [0, 1, 2, 3, 4, 5, 6, 7])
        return opcao

    def pega_dados_cachorro(self):
        print("----- DADOS CACHORRO -----")
        numero_chip = self.valida_inteiro("Numero do Chip: ")
        numero_chip = \
            self.transforma_string_adiciona_caracter_frente("C",
                                                            numero_chip)
        nome = self.valida_num_strig("Nome: ")
        raca = self.valida_num_strig("Raça: ")
        tamanho = self.valida_tamanho("Tamanho: ")

        return {"numero_chip": numero_chip, "nome": nome,
                "raca": raca, "tamanho": tamanho}

    def mostra_cachorro(self, dados_cachorro):
        print("CACHORRO: ")
        print("NÚMERO DO CHIP: ", dados_cachorro["numero_chip"])
        print("NOME: ", dados_cachorro["nome"])
        print("RAÇA: ", dados_cachorro["raca"])
        print("TAMANHO: ", dados_cachorro["tamanho"])
        print("\n")

    def seleciona_cachorro(self):
        numero_chip = self.valida_inteiro("Nùmero do chip do cachorro que "
                                          "deseja selecionar "
                                          "(sem o C na frente): ")
        numero_chip = \
            self.transforma_string_adiciona_caracter_frente("C", numero_chip)
        return numero_chip

    def mostra_mensagem(self, msg):
        print(msg)
