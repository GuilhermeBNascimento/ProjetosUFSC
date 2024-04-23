import PySimpleGUI as sg
from limite.tela_abstrata import TelaAbstrata
from datetime import date


class TelaDoacao(TelaAbstrata):
    def __init__(self):
        self.__janela = None
        self.inicia_opcoes()

    def tela_opcoes(self):
        self.inicia_opcoes()
        botao, valores = self.abre_janela()
        if botao is None or botao in ['Cancelar']:
            opcao = 0
        else:
            try:
                opcao = int(botao)
            except:
                sg.PopupOK("Valor inválido")
                opcao = 0
        self.fechar()
        return opcao

    def fechar(self):
        self.__janela.close()

    def inicia_opcoes(self):
        sg.theme('DarkGreen')
        tela_opcoes = [
            [sg.Text("Amigos dos Pets ONG Lar de Cachorros e Gatos")],
            [sg.Text("Escolha sua opção")],
            [sg.Button("Cadastrar Doação", key='1', size=(30, 0))],
            [sg.Button("Editar Doação", key='2', size=(30, 0))],
            [sg.Button("Remover Doação", key='3', size=(30, 0))],
            [sg.Button("Listar Doação", key='4', size=(30, 0))],
            [sg.Button("Relatório de Doações por data", key='5', size=(30, 0))],
            [sg.Button("Retornar", key='0', size=(30, 0))],
            [sg.Cancel('Cancelar', size=(30, 0))]
        ]
        self.__janela = sg.Window("ONG Lar de Cachorros e Gatos").layout(tela_opcoes)

    def pega_dados_doacao(self, dados_doacao_editar={"ano": "", "mes": "", "dia": "", "numero_chip": "", "animal_doado": "", "motivo_doacao": "", "cpf": ""}):
        ano = dados_doacao_editar['ano']
        mes = dados_doacao_editar['mes']
        dia = dados_doacao_editar['dia']
        numero_chip = dados_doacao_editar['numero_chip']
        animal_doado = dados_doacao_editar['animal_doado']
        motivo_doacao = dados_doacao_editar['motivo_doacao']
        cpf = dados_doacao_editar['cpf']

        while True:
            sg.theme("DarkGreen")

            layout = [
                [sg.Text('Ano:', size=(15, 1)), sg.InputText(ano, key='ano')],
                [sg.Text('Mês:', size=(15, 1)), sg.Combo([n+1 for n in range(12)], default_value=mes, key='mes')],
                [sg.Text('Dia:', size=(15, 1)), sg.Combo([n+1 for n in range(31)], default_value=dia, key='dia')],
                [sg.Text('Numero do chip:', size=(15, 1)), sg.InputText(numero_chip, key='numero_chip')],
                [sg.Text('Animal doado:', size=(15, 1)), sg.Combo(["gato", "cachorro"], default_value=animal_doado, key='animal_doado')],
                [sg.Text('CPF Doador:', size=(15, 1)), sg.InputText(cpf, key='cpf')],
                [sg.Text('Motivo da Doação:', size=(15, 1)), sg.InputText(motivo_doacao, key='motivo_doacao')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]

            self.__janela = sg.Window('Cadastrar Doação').Layout(layout)

            botao, valores = self.abre_janela()
            ano = valores['ano']
            mes = valores['mes']
            dia = valores['dia']
            data_doacao = None
            numero_chip = valores['numero_chip']
            animal_doado = valores['animal_doado']
            motivo_doacao = valores['motivo_doacao']
            cpf = valores['cpf']

            self.fechar()
            if botao == 'Cancelar':
                break

            dados_validos = True
            if self.valida_ano(ano, mensagem_erro="Entrada não aceita! Ano Incoreto"):
                ano = int(ano)
                if self.valida_mes(mes, mensagem_erro="Entrada não aceita! Mês Incoreto"):
                    mes = int(mes)
                    if self.valida_dia(dia, mensagem_erro="Entrada não aceita! Dia Incoreto"):
                        dia = int(dia)
                        data_doacao = date(year=int(ano), month=int(mes), day=int(dia))
                    else:
                        dados_validos = False
                else:
                    dados_validos = False
            else:
                dados_validos = False

            if self.valida_inteiro(numero_chip, mensagem_erro="Entrada não aceita! Numero do chip Incoreto"):
                numero_chip = str(numero_chip)
            else:
                dados_validos = False

            if self.valida_num_strig(motivo_doacao, mensagem_erro="Entrada não aceita! Motivo da Doação Incoreto"):
                motivo_doacao = str(motivo_doacao)
            else:
                dados_validos = False

            if self.valida_inteiro(cpf, mensagem_erro="Entrada não aceita!. CPF Incorreto"):
                cpf = int(cpf)
            else:
                dados_validos = False
            if dados_validos:
                break

        return {"ano": ano, "mes": mes, "dia": dia, "data_doacao": data_doacao,
                "numero_chip": numero_chip, "animal_doado": animal_doado,
                "motivo_doacao": motivo_doacao, "cpf": cpf, "opcao": botao}

    def mostra_doacao(self, lista):
        sg.set_options(font=("Arial Bold", 14))
        cabecalho = ['Data da Doacao', 'Numero do chip', 'Animal Doado', 'Motivo da Doacao', 'Doacao',
                     'Animal']
        valores = []
        for doacao in lista:
            valores.append([
                str(doacao['data_doacao']),
                str(doacao['animal_doado']),
                str(doacao['motivo_doacao']),
                str(doacao['nome_doador']),
                str(doacao['numero_chip'])
            ])

        tbl1 = sg.Table(values=valores, headings=cabecalho,
                        auto_size_columns=True,
                        display_row_numbers=False,
                        justification='center', key='-TABLE-',
                        selected_row_colors='white on green',
                        enable_events=False,
                        expand_x=True,
                        expand_y=True,
                        enable_click_events=False)
        layout = [[tbl1]]
        self.__janela = sg.Window("Mostrar doacao", layout, size=(1000, 700), resizable=True)
        self.__janela.read()

    def seleciona_doacao(self):
        cpf = None
        while True:
            sg.theme("DarkGreen")
            layout = [
                [sg.Text('SELECIONAR DOADOR')],
                [sg.Text('Digite o Numero do CPF que deseja selecionar:')],
                [sg.Text('NUMERO DO CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__janela = sg.Window('Seleciona Doador').Layout(layout)

            botao, valores = self.abre_janela()
            self.fechar()
            if botao == 'Cancelar':
                break
            cpf = valores["cpf"]

            if self.valida_inteiro(cpf, mensagem_erro="CPF Incorreto"):
                cpf = int(cpf)
                break
        return cpf

    def pega_data_relatorio(self):
        while True:
            sg.theme("DarkGreen")
            layout = [
                [sg.Text('DATAS DO RELATÓRIO:')],
                [sg.Text('Digite a data inicial do relatório:')],
                [sg.Text('Ano:', size=(15, 1)), sg.InputText(key='ano_inicial')],
                [sg.Text('Mês:', size=(15, 1)), sg.Combo([n + 1 for n in range(12)], key='mes_inicial')],
                [sg.Text('Dia:', size=(15, 1)), sg.Combo([n + 1 for n in range(31)], key='dia_inicial')],
                [sg.Text('Digite a data final do relatório:')],
                [sg.Text('Ano:', size=(15, 1)), sg.InputText(key='ano_final')],
                [sg.Text('Mês:', size=(15, 1)), sg.Combo([n + 1 for n in range(12)], key='mes_final')],
                [sg.Text('Dia:', size=(15, 1)), sg.Combo([n + 1 for n in range(31)], key='dia_final')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__janela = sg.Window('Seleciona Datas Relatorio').Layout(layout)

            botao, valores = self.abre_janela()
            self.fechar()
            if botao == 'Cancelar':
                break
            ano_inicial = valores["ano_inicial"]
            mes_inicial = valores["mes_inicial"]
            dia_inicial = valores["dia_inicial"]
            ano_final = valores["ano_final"]
            mes_final = valores["mes_final"]
            dia_final = valores["dia_final"]
            dados_validos = True

            if self.valida_ano(ano_inicial, mensagem_erro="Entrada não aceita! Ano Incoreto"):
                ano_inicial = int(ano_inicial)
            else:
                dados_validos = False

            if self.valida_ano(ano_final, mensagem_erro="Entrada não aceita! Ano Incoreto"):
                ano_final = int(ano_final)
            else:
                dados_validos = False

            data_inicial = date(year=ano_inicial, month=mes_inicial, day=dia_inicial)
            data_final = date(year=ano_final, month=mes_final, day=dia_final)
            try:
                if data_final > data_inicial and dados_validos:
                    return data_inicial, data_final
                else:
                    raise ValueError
            except ValueError:
                print("Data final dos dados, anterior a data inicial, "
                      "impossível de se criar relatório")

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

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
                print("Tipo de animal não aceito! Tipos de animais possíveis,"
                      " gato e cachorro!")

    def abre_janela(self):
        botao, valores = self.__janela.read()
        return botao, valores