from diretorio_discreto import DiretorioDiscreto
from diretório_continuo import DiretorioContinuo

class Sistema:
    def __init__(self):
        # Dados armazenados
        self.dados = []

        # Diretórios
        self.diretorio_continuo = DiretorioContinuo()
        self.diretorio_discreto = DiretorioDiscreto()

    def inserir_dado(self, dado):
        """Insere um dado no sistema e atualiza os índices, mas verifica se o ID já existe."""
        if self.buscar_por_id(dado['id']):
            print(f"Erro: Dado com ID {dado['id']} já existe! Não foi inserido.")
            return

        # Inserindo o dado na lista de dados
        self.dados.append(dado)

        # Atualizando os diretórios
        self.diretorio_discreto.inserir(dado, dado['cidade'])  # Exemplo: índice por cidade
        self.diretorio_discreto.inserir(dado, dado['profissao'])  # Exemplo: índice por profissão
        faixa_salario = self.obter_faixa_salarial(dado['salario'])
        self.diretorio_continuo.inserir(dado, faixa_salario)

        # Mensagem de sucesso só aparece quando o dado for inserido
        print("Dado inserido com sucesso!")

    def remover_dado(self, id):
        """Remove um dado do sistema pelo ID e atualiza os diretórios."""
        dado = self.buscar_por_id(id)
        if dado:
            # Atualizando os diretórios
            self.diretorio_discreto.remover(dado, dado['cidade'])
            self.diretorio_discreto.remover(dado, dado['profissao'])
            faixa_salario = self.obter_faixa_salarial(dado['salario'])
            self.diretorio_continuo.remover(dado, faixa_salario)

            # Removendo o dado da lista
            self.dados.remove(dado)
            print(f"Dado com ID {id} removido.")
        else:
            print(f"Erro: Dado com ID {id} não encontrado.")

    def listar_dados(self):
        """Lista todos os dados armazenados."""
        if not self.dados:
            print("Nenhum dado encontrado.")
        for dado in self.dados:
            print(dado)

    def buscar_por_id(self, id):
        """Busca um dado pelo ID."""
        return next((dado for dado in self.dados if dado['id'] == id), None)

    def consultar_por_chave(self, chave):
        """Consulta simples por chave discreta (ex: cidade ou profissão)."""
        return self.diretorio_discreto.buscar(chave)

    def consultar_por_faixa(self, faixa):
        """Consulta simples por faixa salarial."""
        return self.diretorio_continuo.buscar(faixa)

    def consultar_combinada(self, chave_discreta, chave_faixa):
        """Consulta combinada por índice discreto e contínuo (ex: cidade e faixa salarial)."""
        dados_discretos = set(self.consultar_por_chave(chave_discreta))
        dados_faixa = set(self.consultar_por_faixa(chave_faixa))
        return list(dados_discretos & dados_faixa)

    def obter_faixa_salarial(self, salario):
        """Determina a faixa salarial para o índice (faixa de valores contínuos)."""
        if salario < 2000:
            return 'baixo'
        elif salario < 5000:
            return 'medio'
        else:
            return 'alto'

    def carregar_dados_iniciais(self):
        """Carrega um conjunto de dados predefinidos no sistema, evitando duplicação."""
        dados_iniciais = [
            {'id': 1, 'nome': 'João', 'idade': 30, 'cidade': 'São Paulo', 'salario': 2500, 'profissao': 'Engenheiro'},
            {'id': 2, 'nome': 'Maria', 'idade': 28, 'cidade': 'Rio de Janeiro', 'salario': 4000, 'profissao': 'Médica'},
            {'id': 3, 'nome': 'Carlos', 'idade': 35, 'cidade': 'São Paulo', 'salario': 6000, 'profissao': 'Advogado'},
            {'id': 4, 'nome': 'Ana', 'idade': 40, 'cidade': 'Criciúma', 'salario': 1800, 'profissao': 'Professor'},
            {'id': 5, 'nome': 'Lucas', 'idade': 25, 'cidade': 'Criciúma', 'salario': 2000, 'profissao': 'Engenheiro'},
            {'id': 6, 'nome': 'Fernanda', 'idade': 32, 'cidade': 'São Paulo', 'salario': 4500, 'profissao': 'Médica'}
        ]

        # Carrega apenas se o dado não existir
        for dado in dados_iniciais:
            if not self.buscar_por_id(dado['id']):
                self.inserir_dado(dado)
        print("Dados iniciais carregados com sucesso!")


# Função para interação com o menu
def menu():
    sistema = Sistema()

    # Carregar dados iniciais ao iniciar o sistema
    sistema.carregar_dados_iniciais()

    while True:
        print("\nMenu:")
        print("1. Inserir dado")
        print("2. Remover dado")
        print("3. Listar todos os dados")
        print("4. Consultar dado por ID")
        print("5. Consultar por chave discreta (cidade ou profissão)")
        print("6. Consultar por faixa salarial")
        print("7. Consultar combinada (cidade e faixa salarial)")
        print("8. Carregar dados iniciais")
        print("9. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            # Inserir dado
            id = int(input("ID: "))
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            cidade = input("Cidade: ")
            salario = float(input("Salário: "))
            profissao = input("Profissão: ")

            dado = {'id': id, 'nome': nome, 'idade': idade, 'cidade': cidade, 'salario': salario,
                    'profissao': profissao}
            sistema.inserir_dado(dado)
            print("Dado inserido com sucesso!")

        elif opcao == '2':
            # Remover dado
            id = int(input("Digite o ID para remoção: "))
            sistema.remover_dado(id)

        elif opcao == '3':
            # Listar todos os dados
            sistema.listar_dados()

        elif opcao == '4':
            # Consultar por ID
            id = int(input("Digite o ID para consulta: "))
            dado = sistema.buscar_por_id(id)
            if dado:
                print(dado)
            else:
                print("Dado não encontrado.")

        elif opcao == '5':
            # Consultar por chave discreta (cidade ou profissão)
            chave = input("Digite a chave para consulta (cidade ou profissão): ")
            dados = sistema.consultar_por_chave(chave)
            if dados:
                for dado in dados:
                    print(dado)
            else:
                print("Nenhum dado encontrado para esta chave.")

        elif opcao == '6':
            # Consultar por faixa salarial
            faixa = input("Digite a faixa salarial (baixo, medio, alto): ")
            dados = sistema.consultar_por_faixa(faixa)
            if dados:
                for dado in dados:
                    print(dado)
            else:
                print("Nenhum dado encontrado para esta faixa salarial.")

        elif opcao == '7':
            # Consultar combinada
            chave_discreta = input("Digite a chave discreta (cidade ou profissão): ")
            chave_faixa = input("Digite a faixa salarial (baixo, medio, alto): ")
            dados = sistema.consultar_combinada(chave_discreta, chave_faixa)
            if dados:
                for dado in dados:
                    print(dado)
            else:
                print("Nenhum dado encontrado para essa combinação.")

        elif opcao == '8':
            # Carregar dados iniciais
            sistema.carregar_dados_iniciais()

        elif opcao == '9':
            # Sair
            print("Saindo...")
            break

        else:
            print("Opção inválida! Tente novamente.")


menu()



