import PySimpleGUI as sg
from limite.tela_abstrata import TelaAbstrata


class TelaGato(TelaAbstrata):

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
            [sg.Button("Cadastrar Gato", key='1', size=(30, 0))],
            [sg.Button("Editar Gato", key='2', size=(30, 0))],
            [sg.Button("Remover Gato", key='3', size=(30, 0))],
            [sg.Button("Listar Gato", key='4', size=(30, 0))],
            [sg.Button("Listar Gatos Disponiveis", key='5', size=(30, 0))],
            [sg.Button("Vacinas", key='6', size=(30, 0))],
            [sg.Button("Retornar", key='0', size=(30, 0))],
            [sg.Cancel('Cancelar', size=(30, 0))]
        ]
        self.__janela = sg.Window("ONG Lar de Cachorros e Gatos").layout(tela_opcoes)


    def pega_dados_gato(self, dados_gato_editar = {"numero_chip": "", "nome": "", "raca": "", "cor_pelo": ""}):

        numero_chip = dados_gato_editar['numero_chip']
        nome = dados_gato_editar['nome']
        raca = dados_gato_editar['raca']
        cor_pelo = dados_gato_editar['cor_pelo']

        while True:
            sg.theme("DarkGreen")

            layout = [
                [sg.Text('Numero Chip:', size=(15, 1)), sg.InputText(numero_chip, key='numero_chip')],
                [sg.Text('Nome:', size=(15, 1)), sg.InputText(nome, key='nome')],
                [sg.Text('Raca:', size=(15, 1)), sg.InputText(raca, key='raca')],
                [sg.Text('Cor do Pelo:', size=(15, 1)), sg.InputText(cor_pelo, key='cor_pelo')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]

            self.__janela = sg.Window('Cadastrar Gatos').Layout(layout)

            botao, valores = self.abre_janela()
            numero_chip = valores['numero_chip']
            nome = valores['nome']
            raca = valores['raca']
            cor_pelo = valores['cor_pelo']

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

            if self.valida_num_strig(cor_pelo, mensagem_erro="Entrada não aceita! Cor do pelo Incoreto"):
                cor_pelo = str(cor_pelo)
            else:
                dados_validos = False
            if dados_validos:
                break

        return {"numero_chip": numero_chip, "nome": nome, "raca": raca, "cor_pelo": cor_pelo, "opcao": botao}

    def mostra_gato(self, gatos):
        sg.set_options(font=("Arial Bold", 14))
        cabecalho = ['Número do chip', 'Nome', 'Raça', 'Cor do Pelo']
        valores = []
        for gato in gatos:
            valores.append([
                str(gato['numero_chip']),
                str(gato['nome']),
                str(gato['raca']),
                str(gato['cor_pelo'])
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
        self.__janela = sg.Window("Mostrar Gato", layout, size=(715, 200), resizable=True)
        self.__janela.read()

    def seleciona_gato(self):
        numero_chip = None
        while True:
            sg.theme("DarkGreen")
            layout = [
                [sg.Text('SELECIONAR GATO')],
                [sg.Text('Digite o Numero do chip que deseja selecionar:', font=("Helvica", 15))],
                [sg.Text('NUMERO CHIP:', size=(15, 1)), sg.InputText('', key='numero_chip')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__janela = sg.Window('Seleciona Gato').Layout(layout)

            botao, valores = self.abre_janela()
            self.fechar()
            if botao == 'Cancelar':
                break
            numero_chip = valores["numero_chip"]




            if self.valida_inteiro(numero_chip, mensagem_erro="Numero Chipe Incorreto"):
                numero_chip = int(numero_chip)
                break
        return numero_chip

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def abre_janela(self):
        botao, valores = self.__janela.read()
        return botao, valores