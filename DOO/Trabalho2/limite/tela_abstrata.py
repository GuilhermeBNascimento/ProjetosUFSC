from abc import ABC
from datetime import date
import PySimpleGUI as sg
from excecao.ano_errado_exception import AnoErradoException
from excecao.string_com_num_exception import StringComNumeroException


class TelaAbstrata(ABC):
    def valida_inteiro(self, valor_lido: int, mensagem_erro="", ints_validos=None):
        try:
            valor_int = int(valor_lido)
            if ints_validos and valor_int not in ints_validos:
                raise ValueError
            return valor_int
        except ValueError:
            sg.PopupOK(mensagem_erro)
            if ints_validos:
                sg.PopupOK("Valores válidos: ", ints_validos)

    def valida_ano(self, ano_informado: int, mensagem_erro='', ints_validos=None):
        if ano_informado != "":
            ano_informado = int(ano_informado)
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
                raise AnoErradoException(mensagem_erro)

    def valida_mes(self, mes_informado: int, mensagem_erro = '', ints_validos=None):
        if mes_informado != "":
            mes_informado = int(mes_informado)
            try:
                if mes_informado > 12:
                    raise ValueError
                elif mes_informado < 1:
                    raise ValueError
                return mes_informado
            except ValueError:
                sg.PopupOK(mensagem_erro)

    def valida_dia(self, dia_informado: int,mensagem_erro=" ", ints_validos=None):
        if dia_informado != "":
            dia_informado = int(dia_informado)
            try:
                if dia_informado > 31:
                    raise ValueError
                elif dia_informado < 1:
                    raise ValueError
                return dia_informado
            except ValueError:
                sg.PopupOK(mensagem_erro)

    def valida_num_strig(self, valor_lido: str, mensagem_erro=" "):
            try:
                valor_str = str(valor_lido)
                for character in valor_lido:
                    if character.isnumeric():
                        raise ValueError
                    else:
                        return valor_str
            except ValueError:
                raise StringComNumeroException(mensagem_erro)

    def valida_tamanho(self, tamanho_lido: str, mensagem_erro=" "):
            tamanhos_possiveis = ["PEQUENA", "MEDIA", "MÉDIA", "PEQUENO",
                                  "MEDIO", "MÉDIO", "GRANDE", "pequena", "media",
                                  "média", "pequeno", "medio", "médio", "grande"]
            try:
                tamanho_lido = tamanho_lido.upper()
                if tamanho_lido not in tamanhos_possiveis:
                    raise ValueError
                return tamanho_lido
            except ValueError:
                sg.PopupOK(mensagem_erro)

    def transforma_string_adiciona_caracter_frente(self, caracter="",
                                                   numero_chip=None):
        if numero_chip is not None:
            numero_chip = str(numero_chip)
            numero_chip = caracter + numero_chip
            return numero_chip

    def valida_animal(self,  tipo_animal_lido: str, mensagem_erro=" "):
            tipos_animais_possiveis = ["GATO", "CACHORRO", "gato", "cachorro"]
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
                sg.PopupOK(mensagem_erro)

    def valida_habitacao(self, habitacao_lida: str,  mensagem_erro=" "):
            habitacoes_possiveis = ["APARTAMENTO", "CASA", "apartamento", "casa"]
            try:
                habitacao_lida = habitacao_lida.upper()
                if habitacao_lida not in habitacoes_possiveis:
                    raise ValueError
                return habitacao_lida
            except ValueError:
                sg.PopupOK(mensagem_erro)

    def valida_propriedade_animal(self, propriedade_animal: str, mensagem_erro=" "):
            opcoes_possiveis = ["SIM", "NAO", "NÃO", "sim", "nao", "não"]
            try:
                propriedade_animal = propriedade_animal.upper()
                if propriedade_animal not in opcoes_possiveis:
                    raise ValueError
                return propriedade_animal
            except ValueError:
                sg.PopupOK(mensagem_erro)

    def termo_responsabilidade(self, resposta_lida: str, mensagem_erro=""):
            respostas_possiveis = ["SIM", "NAO", "sim", "nao"]
            try:
                resposta_lida = resposta_lida.upper()
                if resposta_lida not in respostas_possiveis:
                    raise ValueError
                if resposta_lida == "SIM":
                    return resposta_lida
                else:
                    sg.PopupOK("Para concluir a adoção você precisa "
                          "assinar esse termo")
            except ValueError:
                sg.PopupOK(mensagem_erro)