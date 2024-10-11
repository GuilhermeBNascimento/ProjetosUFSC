from no import NO

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.__inicio = None
        self.__fim = None
        self.__cursor = None

    def acessar_atual(self):
        if self.__cursor:
            print(f'Valor atual: {self.__cursor.valor}')

    def inserir_antes_do_atual(self, novo):
        novo_no = NO(novo)
        if not self.__cursor:
            return None  # Não faz nada se o cursor for None
        novo_no.proximo = self.__cursor
        novo_no.anterior = self.__cursor.anterior
        if self.__cursor.anterior:
            self.__cursor.anterior.proximo = novo_no
        else:
            self.__inicio = novo_no  # Atualiza a cabeça se estiver inserindo antes do primeiro elemento
        self.__cursor.anterior = novo_no

    def inserir_apos_atual(self, novo):
        novo_no = NO(novo)
        if not self.__cursor:
            return None  # Não faz nada se o cursor for None
        novo_no.anterior = self.__cursor
        novo_no.proximo = self.__cursor.proximo
        self.__cursor.proximo = novo_no
        if novo_no.proximo:
            novo_no.proximo.anterior = novo_no
        else:
            self.__fim = novo_no  # Atualiza a cauda se estiver inserindo após o último elemento

    def inserir_como_ultimo(self, novo):
        novo_no = NO(novo)
        if not self.__inicio:
            self.__inicio = novo_no
            self.__fim = novo_no
        else:
            self.__fim.proximo = novo_no
            novo_no.anterior = self.__fim
            self.__fim = novo_no

    def inserir_como_primeiro(self, novo):
        novo_no = NO(novo)
        if not self.__inicio:
            self.__inicio = novo_no
            self.__fim = novo_no
        else:
            novo_no.proximo = self.__inicio
            self.__inicio.anterior = novo_no
            self.__inicio = novo_no

    def inserir_na_posicao(self, k, novo):
        if k == 0:
            self.inserir_como_primeiro(novo)
            return None
        novo_no = NO(novo)
        atual = self.__inicio
        for _ in range(k):
            if not atual:
                break
            atual = atual.proximo
        if atual:
            novo_no.anterior = atual.anterior
            novo_no.proximo = atual
            if atual.anterior:
                atual.anterior.proximo = novo_no
            else:
                self.__inicio = novo_no
            atual.anterior = novo_no
        else:
            self.inserir_como_ultimo(novo)

    def excluir_atual(self):
        if not self.__cursor:
            return None
        if self.__cursor.anterior:
            self.__cursor.anterior.proximo = self.__cursor.proximo
        else:
            self.__inicio = self.__cursor.proximo
        if self.__cursor.proximo:
            self.__cursor.proximo.anterior = self.__cursor.anterior
        else:
            self.__fim = self.__cursor.anterior
        self.__cursor = self.__cursor.proximo  # Mover o cursor para o próximo elemento

    def excluir_prim(self):
        if not self.__inicio:
            return
        self.__cursor = self.__inicio
        self.excluir_atual()

    def excluir_ult(self):
        if not self.__fim:
            return None
        self.__cursor = self.__fim
        self.excluir_atual()

    def excluir_elem(self, chave):
        atual = self.__inicio
        while atual:
            if atual.valor == chave:
                self.__cursor = atual
                self.excluir_atual()
                return None
            atual = atual.proximo

    def excluir_da_pos(self, k):
        atual = self.__inicio
        for _ in range(k):
            if not atual:
                return None
            atual = atual.proximo
        if atual:
            self.__cursor = atual
            self.excluir_atual()

    def buscar(self, chave):
        atual = self.__inicio
        while atual:
            if atual.valor == chave:
                return print("O valor encontrado foi: ", atual.valor)
            atual = atual.proximo
        return print("Valor não encontrado!")

    def exibir(self):
        atual = self.__inicio
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
        self.__cursor = self.__inicio

    def ir_para_ultimo(self):
        self.__cursor = self.__fim