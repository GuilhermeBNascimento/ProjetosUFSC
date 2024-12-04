from estudante import Estudante
from getordados import GestorDeDados

def menu():
    while True:
        print("1. Carga de dados")
        print("2. Consulta simples")
        print("3. Consulta composta")
        print("4. Inclusão de novo elemento")
        print("5. Buscar por ID")
        print("6. Remover por ID")
        print("7. Exibir todos os dados")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            gestor = GestorDeDados()
            gestor.inserir(Estudante(1, "123", "João", "Engenharia", "Criciúma", "Figueirense"))
            gestor.inserir(Estudante(2, "124", "Maria", "Medicina", "Florianópolis", "Grêmio"))
        elif opcao == "2":
            campo = input("Escolha o campo (matricula, curso, time_torce, cidade_origem): ")
            valor = input(f"Informe o valor para {campo}: ")
            resultado = gestor.consulta_simples(campo, valor)
            print("Resultado:", resultado)
        elif opcao == "3":
            campo1 = input("Escolha o primeiro campo (matricula, curso, time_torce, cidade_origem): ")
            valor1 = input(f"Informe o valor para {campo1}: ")
            campo2 = input("Escolha o segundo campo (matricula, curso, time_torce, cidade_origem): ")
            valor2 = input(f"Informe o valor para {campo2}: ")
            resultado = gestor.consulta_composta(campo1, valor1, campo2, valor2)
            print("Resultado:", resultado)
        elif opcao == "4":
            id = input("Informe o ID: ")
            matricula = input("Informe a matrícula: ")
            nome = input("Informe o nome: ")
            curso = input("Informe o curso: ")
            cidade_origem = input("Informe a cidade de origem: ")
            time_torce = input("Informe o time que torce: ")
            novo_elemento = Estudante(int(id), matricula, nome, curso, cidade_origem, time_torce)
            gestor.inserir(novo_elemento)
        elif opcao == "5":
            id = int(input("Informe o ID para busca: "))
            elemento = gestor.buscar_por_id(id)
            print("Elemento encontrado:", vars(elemento) if elemento else "Não encontrado")
        elif opcao == "6":
            id = int(input("Informe o ID para remover: "))
            gestor.excluir_por_id(id)
        elif opcao == "7":
            gestor.exibir_dados()
        elif opcao == "0":
            break

menu()
