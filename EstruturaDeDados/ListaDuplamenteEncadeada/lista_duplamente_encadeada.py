from no import Nodo

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.__cabeca = None
        self.__cauda = None
        self.__cursor = None

    def acessar_atual(self):
        if self.__cursor:
            print(f'Valor atual: {self.__cursor.valor}')

    def inserir_antes_do_atual(self, novo):
        novo_nodo = Nodo(novo)
        if not self.__cursor:
            return  # Não faz nada se o cursor for None
        novo_nodo.proximo = self.__cursor
        novo_nodo.anterior = self.__cursor.anterior
        if self.__cursor.anterior:
            self.__cursor.anterior.proximo = novo_nodo
        else:
            self.__cabeca = novo_nodo  # Atualiza a cabeça se estiver inserindo antes do primeiro elemento
        self.__cursor.anterior = novo_nodo

    def inserir_após_atual(self, novo):
        novo_nodo = Nodo(novo)
        if not self.__cursor:
            return  # Não faz nada se o cursor for None
        novo_nodo.anterior = self.__cursor
        novo_nodo.proximo = self.__cursor.proximo
        self.__cursor.proximo = novo_nodo
        if novo_nodo.proximo:
            novo_nodo.proximo.anterior = novo_nodo
        else:
            self.__cauda = novo_nodo  # Atualiza a cauda se estiver inserindo após o último elemento

    def inserir_como_ultimo(self, novo):
        novo_nodo = Nodo(novo)
        if not self.__cabeca:
            self.__cabeca = novo_nodo
            self.__cauda = novo_nodo
        else:
            self.__cauda.proximo = novo_nodo
            novo_nodo.anterior = self.__cauda
            self.__cauda = novo_nodo

    def inserir_como_primeiro(self, novo):
        novo_nodo = Nodo(novo)
        if not self.__cabeca:
            self.__cabeca = novo_nodo
            self.__cauda = novo_nodo
        else:
            novo_nodo.proximo = self.cabeca
            self.__cabeca.anterior = novo_nodo
            self.__cabeca = novo_nodo

    def inserir_na_posicao(self, k, novo):
        if k == 0:
            self.inserir_como_primeiro(novo)
            return
        novo_nodo = Nodo(novo)
        atual = self.cabeca
        for _ in range(k):
            if not atual:
                break
            atual = atual.proximo
        if atual:
            novo_nodo.anterior = atual.anterior
            novo_nodo.proximo = atual
            if atual.anterior:
                atual.anterior.proximo = novo_nodo
            else:
                self.__cabeca = novo_nodo
            atual.anterior = novo_nodo
        else:
            self.inserir_como_ultimo(novo)

    def excluir_atual(self):
        if not self.cursor:
            return
        if self.__cursor.anterior:
            self.__cursor.anterior.proximo = self.__cursor.proximo
        else:
            self.__cabeca = self.__cursor.proximo
        if self.__cursor.proximo:
            self.__cursor.proximo.anterior = self.__cursor.anterior
        else:
            self.__cauda = self.__cursor.anterior
        self.__cursor = self.__cursor.proximo  # Mover o cursor para o próximo elemento

    def excluir_prim(self):
        if not self.__cabeca:
            return
        self.__cursor = self.__cabeca
        self.excluir_atual()

    def excluir_ult(self):
        if not self.__cauda:
            return
        self.__cursor = self.__cauda
        self.excluir_atual()

    def excluir_elem(self, chave):
        atual = self.__cabeca
        while atual:
            if atual.valor == chave:
                self.__cursor = atual
                self.excluir_atual()
                return
            atual = atual.proximo

    def excluir_da_pos(self, k):
        atual = self.__cabeca
        for _ in range(k):
            if not atual:
                return
            atual = atual.proximo
        if atual:
            self.__cursor = atual
            self.excluir_atual()

    def buscar(self, chave):
        atual = self.__cabeca
        while atual:
            if atual.valor == chave:
                return True
            atual = atual.proximo
        return False

    def exibir(self):
        atual = self.__cabeca
        while atual:
            print(atual.valor, end=' ')
            atual = atual.proximo
        print()

    def avancar_k_posicoes(self, k):
        for _ in range(k):
            if self.__cursor and self.__cursor.proximo:
                self.__cursor = self.__cursor.proximo
            else:
                break  # Para se chegar ao final da lista

    def retroceder_k_posicoes(self, k):
        for _ in range(k):
            if self.__cursor and self.__cursor.anterior:
                self.__cursor = self.__cursor.anterior
            else:
                break  # Para se chegar ao início da lista

    def ir_para_primeiro(self):
        self.__cursor = self.__cabeca

    def ir_para_ultimo(self):
        self.__cursor = self.__cauda