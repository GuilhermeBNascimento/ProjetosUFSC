from multilista import Multilista
from diretorio_discreto import DiretorioDiscreto
from diretorio_continuo import DiretorioContínuo
from veiculo import Veiculo

def main():
    # Instâncias das classes
    multilista = Multilista()
    diretorio_marca = DiretorioDiscreto()
    diretorio_modelo = DiretorioDiscreto()
    diretorio_preco = DiretorioContínuo()

    def carregar_dados():
        dados = [
            Veiculo(1, "Toyota", "Corolla", 2020, "São Paulo", 90000),
            Veiculo(2, "Ford", "Fiesta", 2018, "Rio de Janeiro", 45000),
            Veiculo(3, "Chevrolet", "Onix", 2021, "Belo Horizonte", 75000),
        ]
        for veiculo in dados:
            if multilista.inserir(veiculo):
                diretorio_marca.indexar(veiculo, "marca")
                diretorio_modelo.indexar(veiculo, "modelo")
                diretorio_preco.indexar(veiculo, "preco")

    def incluir_veiculo():
        identificador = int(input("Identificador: "))
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        ano = input("Ano: ")
        cidade = input("Cidade: ")
        preco = float(input("Preco: "))
        veiculo = Veiculo(identificador, marca, modelo, ano, cidade, preco)
        if multilista.inserir(veiculo):
            diretorio_marca.indexar(veiculo, "marca")
            diretorio_modelo.indexar(veiculo, "modelo")
            diretorio_preco.indexar(veiculo, "preco")
            print("Elemento adicionado com sucesso.")

    def consulta_simples():
        campo = input("Escolha o campo (marca, modelo ou preco): ")
        if campo == "marca":
            valor = input("Informe a marca: ")
            resultado = diretorio_marca.consultar(valor)
        elif campo == "modelo":
            valor = input("Informe o modelo: ")
            resultado = diretorio_modelo.consultar(valor)
        elif campo == "preco":
            min_val = float(input("Preco mínimo: "))
            max_val = float(input("Preco máximo: "))
            resultado = diretorio_preco.consultar(min_val, max_val)
        else:
            print("Campo inválido.")
            return
        for e in resultado:
            print(vars(e))

    def consulta_composta():
        print("Escolha dois campos: (marca e modelo), (marca e preco), (modelo e preco)")
        campos = input("Exemplo: marca e modelo -> ").split(" e ")
        if "marca" in campos and "modelo" in campos:
            marca = input("Informe a marca: ")
            modelo = input("Informe o modelo: ")
            resultado = [v for v in diretorio_marca.consultar(marca) if v in diretorio_modelo.consultar(modelo)]
        elif "marca" in campos and "preco" in campos:
            marca = input("Informe a marca: ")
            min_val = float(input("Preço mínimo: "))
            max_val = float(input("Preço máximo: "))
            resultado = [v for v in diretorio_marca.consultar(marca) if
                         v in diretorio_preco.consultar(min_val, max_val)]
        elif "modelo" in campos and "preco" in campos:
            modelo = input("Informe o modelo: ")
            min_val = float(input("Preço mínimo: "))
            max_val = float(input("Preço máximo: "))
            resultado = [v for v in diretorio_modelo.consultar(modelo) if
                         v in diretorio_preco.consultar(min_val, max_val)]
        else:
            print("Combinação inválida.")
            return
        for v in resultado:
            print(vars(v))

    def buscar_por_identificador():
        identificador = int(input("Identificador: "))
        veiculo = multilista.buscar(identificador)
        if veiculo:
            print(vars(veiculo))
        else:
            print("Veiculo não encontrado.")

    def remover_veiculo():
        identificador = int(input("Identificador: "))
        veiculo = multilista.remover(identificador)
        if veiculo:
            print("Veiculo removido com sucesso.")
        else:
            print("Veiculo não encontrado.")

    def listar_todos():
        for elemento in multilista.listar_todos():
            print(vars(elemento))

    # Menu
    while True:
        print("\nMenu:")
        print("1. Carga de dados")
        print("2. Consulta simples")
        print("3. Consulta composta")
        print("4. Incluir novo veiculo")
        print("5. Buscar veiculo por identificador")
        print("6. Remover veiculo por identificador")
        print("7. Listar todos os veiculos")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            carregar_dados()
        elif opcao == "2":
            consulta_simples()
        elif opcao == "3":
            consulta_composta()
        elif opcao == "4":
            incluir_veiculo()
        elif opcao == "5":
            buscar_por_identificador()
        elif opcao == "6":
            remover_veiculo()
        elif opcao == "7":
            listar_todos()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
