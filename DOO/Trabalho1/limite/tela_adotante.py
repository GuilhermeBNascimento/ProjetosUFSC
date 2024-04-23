from limite.tela_abstrata import TelaAbstrata
from datetime import date


class TelaAdotante(TelaAbstrata):
    def tela_opcoes(self):
        print("----- Registar Adotante -----")
        print("Escolha sua opção: ")
        print("1 - Cadastrar Adotante")
        print("2 - Editar Adotante")
        print("3 - Remover Adotante")
        print("4 - Listar Adotante")
        print("5 - Procurar Adotante")
        print("0 - Retornar")
        opcao = self.valida_inteiro("Escolha a opção:", [0, 1, 2, 3, 4, 5])
        return opcao

    def pega_dados_adotante(self):
        print("----- DADOS ADOTANTE -----")
        nome = self.valida_num_strig("Nome Adotante:")
        cpf = self.valida_inteiro("CPF Adotante:")
        ano = self.valida_ano("Ano de Nascimento:")
        mes = self.valida_mes("Mês de Nascimento:")
        dia = self.valida_dia("Dia de Nascimento:")
        data_nascimento = date(year=ano, month=mes, day=dia)
        endereco = input("Endereço Adotante:")
        tipo_habitacao = self.valida_habitacao("Tipo da habitação do adotante"
                                               "(Apartamento ou Casa):")
        tamanho_residencia = self.valida_tamanho("Tamanho da residência "
                                                 "(Pequena, Média ou Grande):")
        possui_animal = self.valida_propriedade_animal("Possui animal?"
                                                       "(Sim ou Não):")

        return {"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento,
                "endereco": endereco, "tipo_habitacao": tipo_habitacao,
                "tamanho_residencia": tamanho_residencia,
                "possui_animal": possui_animal}

    def mostra_adotante(self, dados_adotante):
        print("ADOTANTE: ")
        print("NOME: ", dados_adotante["nome"])
        print("CPF: ", dados_adotante["cpf"])
        print("DATA DE NASCIMENTO: ", dados_adotante["data_nascimento"])
        print("ENDEREÇO: ", dados_adotante["endereco"])
        print("TIPO DE HABITAÇÃO: ", dados_adotante["tipo_habitacao"])
        print("TAMANHO DA RESIDÊNCIA: ", dados_adotante["tamanho_residencia"])
        print("POSSUI ANIMAL: ", dados_adotante["possui_animal"])
        print("\n")

    def seleciona_adotante(self):
        cpf_adotante = self.valida_inteiro("CPF do adotante que "
                                           "deseja selecionar: ")
        return cpf_adotante

    def mostra_mensagem(self, msg):
        print(msg)

    def valida_habitacao(self, mensagem=" "):
        while True:
            habitacao_lida = input(mensagem)
            habitacoes_possiveis = ["APARTAMENTO", "CASA"]
            try:
                habitacao_lida = habitacao_lida.upper()
                if habitacao_lida not in habitacoes_possiveis:
                    raise ValueError
                return habitacao_lida
            except ValueError:
                print("Habitação informada não aceita! Habitações válidas,"
                      " apartamento e casa!")

    def valida_tamanho(self, mensagem=" "):
        while True:
            tamanho_lido = input(mensagem)
            tamanhos_possiveis = ["PEQUENA", "MEDIA", "MÉDIA", "PEQUENO",
                                  "MEDIO", "MÉDIO", "GRANDE"]
            try:
                tamanho_lido = tamanho_lido.upper()
                if tamanho_lido not in tamanhos_possiveis:
                    raise ValueError
                return tamanho_lido
            except ValueError:
                print("Tamanho informado não aceito! Tamanhos válidos,"
                      " pequena, média e grande!")

    def valida_propriedade_animal(self, mensagem=" "):
        while True:
            propriedade_animal = input(mensagem)
            opcoes_possiveis = ["SIM", "NAO", "NÃO"]
            try:
                propriedade_animal = propriedade_animal.upper()
                if propriedade_animal not in opcoes_possiveis:
                    raise ValueError
                return propriedade_animal
            except ValueError:
                print("Opção informada não aceita! Respostas "
                      "possíveis, sim ou não!")
