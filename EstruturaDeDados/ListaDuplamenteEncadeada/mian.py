from lista_duplamente_encadeada import ListaDuplamenteEncadeada

if __name__ == "__main__":
    lista = ListaDuplamenteEncadeada()
    lista.inserir_como_primeiro(90)
    lista.inserir_como_ultimo(1)
    lista.inserir_como_ultimo(2)
    lista.inserir_como_ultimo(3)
    lista.inserir_como_ultimo(4)
    lista.inserir_como_ultimo(5)
    lista.exibir()  # Saída: 1 2 3 4 5

    lista.ir_para_primeiro()
    lista.acessar_atual()  # Saída: 1

    lista.avancar_k_posicoes(2)
    lista.acessar_atual()  # Saída: 3

    lista.retroceder_k_posicoes(1)
    lista.acessar_atual()  # Saída: 2

    lista.ir_para_ultimo()
    lista.acessar_atual()  # Saída: 5

    print("--------------------")