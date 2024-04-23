from abc import ABC
from datetime import date


class TelaAbstrata(ABC):
    def valida_inteiro(self, mensagem=" ", ints_validos=None):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_int = int(valor_lido)
                if ints_validos and valor_int not in ints_validos:
                    raise ValueError
                return valor_int
            except ValueError:
                print("Valor incorreto!")
                if ints_validos:
                    print("Valores válidos: ", ints_validos)

    def valida_ano(self, mensagem=" ", ints_validos=None):
        while True:
            ano_informado = self.valida_inteiro(mensagem, ints_validos)
            data = date.today()
            ano_atual = data.year
            try:
                diferenca = ano_atual - ano_informado
                if ano_informado > ano_atual:
                    raise ValueError
                elif diferenca > 200:
                    raise ValueError
                return ano_informado
            except ValueError:
                print("Valor para ano não aceito")

    def valida_mes(self, mensagem=" ", ints_validos=None):
        while True:
            mes = self.valida_inteiro(mensagem, ints_validos)
            try:
                if mes > 12:
                    raise ValueError
                elif mes < 1:
                    raise ValueError
                return mes
            except ValueError:
                print("Valor para mes não aceito")

    def valida_dia(self, mensagem=" ", ints_validos=None):
        while True:
            dia = self.valida_inteiro(mensagem, ints_validos)
            try:
                if dia > 31:
                    raise ValueError
                elif dia < 1:
                    raise ValueError
                return dia
            except ValueError:
                print("Valor para dia não aceito")

    def valida_num_strig(self, mensagem=" "):
        while True:
            valor_lido = input(mensagem)
            try:
                for character in valor_lido:
                    if character.isnumeric():
                        raise ValueError
                    else:
                        return valor_lido
            except ValueError:
                print("Entrada não aceita! Algum caracter estranho")

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

    def transforma_string_adiciona_caracter_frente(self, caracter="",
                                                   numero_chip=None):
        if numero_chip is not None:
            numero_chip = str(numero_chip)
            numero_chip = caracter + numero_chip
            return numero_chip

    def valida_animal(self, mensagem=" "):
        while True:
            tipo_animal_lido = input(mensagem)
            tipos_animais_possiveis = ["GATO", "CACHORRO"]
            try:
                tipo_animal_lido = tipo_animal_lido.upper()
                if tipo_animal_lido not in tipos_animais_possiveis:
                    raise ValueError
                if tipo_animal_lido == "GATO":
                    tipo_animal_lido = "G"
                    return tipo_animal_lido
                else:
                    tipo_animal_lido = "C"
                    return tipo_animal_lido
            except ValueError:
                print("Tipo de animal não aceito! Tipos de animais"
                      " possíveis, gato e cachorro!")
