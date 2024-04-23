from limite.tela_abstrata import TelaAbstrata


class TelaSistema(TelaAbstrata):
    def tela_opcoes(self):
        print("----- Amigos dos Pets ONG Lar de Cachorros e Gatos -----")
        print("Escolha sua opção:")
        print("1 - Registrar Adoção e Ler seus Relatórios")
        print("2 - Registrar Doação e Ler seus Relatórios")
        print("3 - Cadastrar Adotante")
        print("4 - Cadastrar Doador")
        print("5 - Cadastrar Cachorro")
        print("6 - Cadastrar Gato")
        print("0 - Encerrar Sistema")
        opcao = self.valida_inteiro("Escolha a opção:", [0, 1, 2, 3, 4, 5, 6])
        return opcao
