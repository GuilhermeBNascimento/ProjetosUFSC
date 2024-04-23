import PySimpleGUI as sg
from limite.tela_abstrata import TelaAbstrata
from datetime import date


class TelaDoador(TelaAbstrata):

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
            [sg.Button("Cadastrar Doador", key='1', size=(30, 0))],
            [sg.Button("Editar Doador", key='2', size=(30, 0))],
            [sg.Button("Remover Doador", key='3', size=(30, 0))],
            [sg.Button("Listar Doador", key='4', size=(30, 0))],
            [sg.Button("Retornar", key='0', size=(30, 0))],
            [sg.Cancel('Cancelar', size=(30, 0))]
        ]
        self.__janela = sg.Window("ONG Lar de Cachorros e Gatos").layout(tela_opcoes)

    def pega_dados_doador(self, dados_doador_editar = {"nome": "", "cpf": "", "endereco": "", "ano": "", "mes": "", "dia": "", "telefone": ""}):
        nome = dados_doador_editar['nome']
        cpf = dados_doador_editar['cpf']
        endereco = dados_doador_editar['endereco']
        ano = dados_doador_editar['ano']
        mes = dados_doador_editar['mes']
        dia = dados_doador_editar['dia']
        telefone = dados_doador_editar['telefone']

        while True:
            sg.theme("DarkGreen")

            layout = [
                [sg.Text('Nome:', size=(15, 1)), sg.InputText(nome, key='nome')],
                [sg.Text('CPF:', size=(15, 1)), sg.InputText(cpf, key='cpf')],
                [sg.Text('Ano:', size=(15, 1)), sg.InputText(ano, key='ano')],
                [sg.Text('Mês:', size=(15, 1)), sg.Combo([n+1 for n in range(12)], default_value=mes, key='mes')],
                [sg.Text('Dia:', size=(15, 1)), sg.Combo([n+1 for n in range(31)], default_value=dia, key='dia')],
                [sg.Text('Endereço:', size=(15, 1)), sg.InputText(endereco, key='endereco')],
                [sg.Text('Telefone:', size=(15, 1)), sg.InputText(cpf, key='telefone')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]

            self.__janela = sg.Window('Cadastrar Doador').Layout(layout)

            botao, valores = self.abre_janela()
            nome = valores['nome']
            cpf = valores['cpf']
            ano = valores['ano']
            mes = valores['mes']
            dia = valores['dia']
            data_nascimento = None
            endereco = valores['endereco']
            telefone = valores['telefone']

            self.fechar()
            if botao == 'Cancelar':
                break

            dados_validos = True
            if self.valida_num_strig(nome, mensagem_erro="Entrada não aceita! Nome Incorreto"):
                nome = str(nome)
            else:
                dados_validos = False

            if self.valida_inteiro(cpf, mensagem_erro="Entrada não aceita! CPF Incorreto"):
                cpf = int(cpf)
            else:
                dados_validos = False

            if self.valida_ano(ano, mensagem_erro="Entrada não aceita! Ano Incoreto"):
                ano = int(ano)
                if self.valida_mes(mes, mensagem_erro="Entrada não aceita! Mês Incoreto"):
                    mes = int(mes)
                    if self.valida_dia(dia, mensagem_erro="Entrada não aceita! Dia Incoreto"):
                        dia = int(dia)
                        data_nascimento = date(year=int(ano), month=int(mes), day=int(dia))
                    else:
                        dados_validos = False
                else:
                    dados_validos = False
            else:
                dados_validos = False

            if self.valida_num_strig(endereco, mensagem_erro="Entrada não aceita! Endereço Incoreto"):
                endereco = str(endereco)
            else:
                dados_validos = False

            if self.valida_inteiro(telefone, mensagem_erro="Entrada não aceita! Telefone Incorreto"):
                telefone = int(telefone)
            else:
                dados_validos = False

            if dados_validos:
                break

        return {"nome": nome, "cpf": cpf, "ano": ano, "mes": mes,
                "dia": dia, "data_nascimento": data_nascimento,
                "endereco": endereco, "telefone": telefone, "opcao": botao}

    def mostra_doador(self, doadores):
        sg.set_options(font=("Arial Bold", 14))
        cabecalho = ['Nome', 'CPF', 'Data de Nascimento', 'Endereço',
                     'Telefone']
        valores = []
        for doador in doadores:
            valores.append([
                str(doador['nome']),
                str(doador['cpf']),
                str(doador['data_nascimento']),
                str(doador['endereco']),
                str(doador['telefone']),
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
        self.__janela = sg.Window("Mostrar doador", layout, size=(1000, 700), resizable=True)
        self.__janela.read()

    def seleciona_doador(self):
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

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def abre_janela(self):
        botao, valores = self.__janela.read()
        return botao, valores
