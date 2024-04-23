import PySimpleGUI as sg
from limite.tela_abstrata import TelaAbstrata


class TelaCachorro(TelaAbstrata):
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
            [sg.Button("Cadastrar Cachorro", key='1', size=(30, 0))],
            [sg.Button("Editar Cachorro", key='2', size=(30, 0))],
            [sg.Button("Remover Cachorro", key='3', size=(30, 0))],
            [sg.Button("Listar Cachorros", key='4', size=(30, 0))],
            [sg.Button("Vacinas", key='6', size=(30, 0))],
            [sg.Button("Listar Cachorros Disponiveis", key='7', size=(30, 0))],
            [sg.Button("Retornar", key='0', size=(30, 0))],
            [sg.Cancel('Cancelar', size=(30, 0))]
        ]
        self.__janela = sg.Window("ONG Lar de Cachorros e Gatos").layout(tela_opcoes)

    def pega_dados_cachorro(self, dados_cachorro_editar = {"numero_chip": "", "nome": "", "raca": "", "tamanho": ""}):

        numero_chip = dados_cachorro_editar['numero_chip']
        nome = dados_cachorro_editar['nome']
        raca = dados_cachorro_editar['raca']
        tamanho = dados_cachorro_editar['tamanho']

        while True:
            sg.theme("DarkGreen")

            layout = [
                [sg.Text('Numero Chip:', size=(15, 1)), sg.InputText(numero_chip, key='numero_chip')],
                [sg.Text('Nome:', size=(15, 1)), sg.InputText(nome, key='nome')],
                [sg.Text('Raca:', size=(15, 1)), sg.InputText(raca, key='raca')],
                [sg.Text('Tamanho:', size=(15, 1)), sg.Combo(["Pequeno", "Médio", "Grande"], default_value=tamanho, key='tamanho')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]

            self.__janela = sg.Window('Cadastrar Cachorros').Layout(layout)

            botao, valores = self.abre_janela()
            numero_chip = valores['numero_chip']
            nome = valores['nome']
            raca = valores['raca']
            tamanho = valores['tamanho']

            self.fechar()
            if botao == 'Cancelar':
                break

            dados_validos = True
            if self.valida_inteiro(numero_chip, mensagem_erro="Numero Chipe Incorreto"):
                numero_chip = str(numero_chip)
            else:
                dados_validos = False

            if self.valida_num_strig(nome, mensagem_erro="Entrada não aceita! Nome Incorreto"):
                nome = str(nome)
            else:
                dados_validos = False

            if self.valida_num_strig(raca, mensagem_erro="Entrada não aceita! Raça Incoreta"):
                raca = str(raca)
            else:
                dados_validos = False

            if dados_validos:
                break

        return {"numero_chip": numero_chip, "nome": nome, "raca": raca, "tamanho": tamanho, "opcao": botao}

    def mostra_cachorro(self, cachorros):
        sg.set_options(font=("Arial Bold", 14))
        cabecalho = ['Número do chip', 'Nome', 'Raça', 'Tamanho']
        valores = []
        for cachorro in cachorros:
            valores.append([
                str(cachorro['numero_chip']),
                str(cachorro['nome']),
                str(cachorro['raca']),
                str(cachorro['tamanho'])
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
        layout = [[tbl1],
                  [sg.Button("Alterar"), sg.Button("Excluir")]]
        self.__janela = sg.Window("Mostrar Cachorro", layout, size=(715, 200), resizable=True)
        self.__janela.read()

    def seleciona_cachorro(self):
        numero_chip = None
        while True:
            sg.theme("DarkGreen")
            layout = [
                [sg.Text('SELECIONAR CACHORRO')],
                [sg.Text('Digite o Numero do chip que deseja selecionar:', font=("Helvica", 15))],
                [sg.Text('NUMERO CHIP:', size=(15, 1)), sg.InputText('', key='numero_chip')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__janela = sg.Window('Seleciona Cachorro').Layout(layout)

            botao, valores = self.abre_janela()
            self.fechar()
            if botao == 'Cancelar':
                break
            numero_chip = valores["numero_chip"]




            if self.valida_inteiro(numero_chip, mensagem_erro="Numero Chipe Incorreto"):
                numero_chip = str(numero_chip)
                break
        return numero_chip

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def abre_janela(self):
        botao, valores = self.__janela.read()
        return botao, valores
