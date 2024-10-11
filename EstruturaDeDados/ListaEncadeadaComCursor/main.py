from lista_duplamente_encadeada import ListaDuplamenteEncadeada

if __name__ == "__main__":
    lista = ListaDuplamenteEncadeada()
    lista.inserir_como_primeiro(10)
    lista.inserir_como_ultimo(20)
    lista.inserir_como_ultimo(30)
    lista.inserir_como_ultimo(40)
    lista.inserir_como_ultimo(50)
    lista.inserir_como_ultimo(60)
    lista.inserir_como_ultimo(70)
    lista.inserir_como_ultimo(80)
    lista.inserir_como_ultimo(90)
    lista.inserir_como_ultimo(100)
    lista.exibir() # Saída: 10 20 30 40 50 60 70 80 90 100

    print("--------------------")

    lista.excluir_prim()
    lista.excluir_ult()
    lista.exibir() # Saída: 20 30 40 50 60 70 80 90

    print("--------------------")

    lista.buscar(20) # Saida: Retorna o 20
    lista.buscar(10) # Saida: Retorna um erro, pois o numero não esta na lista

    print("--------------------")

    lista.ir_para_primeiro() # Saida: vai para o primeiro nó da lista
    lista.acessar_atual() # Saida: Exibi o valor apontado pelo cursor


