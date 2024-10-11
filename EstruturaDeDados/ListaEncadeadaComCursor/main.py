from lista_duplamente_encadeada import ListaDuplamenteEncadeada

if __name__ == "__main__":
    lista = ListaDuplamenteEncadeada()
    lista.inserir_como_primeiro(10)
    lista.inserir_como_ultimo(20)
    lista.inserir_como_ultimo(30)
    lista.inserir_como_ultimo(40)
    lista.inserir_como_ultimo(50)
    lista.exibir()  # Saída: 10 20 30 40 50

    print("--------------------")

    lista.excluir_prim()
    lista.excluir_ult()
    lista.exibir() # Saída: 20 30 40

    print("--------------------")

    lista.buscar(20) # Saida: Retorna o 20
    lista.buscar(10) # Saida: Retorna um erro, pois o numero não esta na lista