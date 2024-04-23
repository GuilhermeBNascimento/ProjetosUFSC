import PySimpleGUI as sg
from limite.tela_abstrata import TelaAbstrata
from datetime import date


class TelaVacina(TelaAbstrata):
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
            [sg.Button("Cadastrar Vacina no Animal Escolhido", key='1', size=(40, 0))],
            [sg.Button("Editar Vacina no Animal Escolhido", key='2', size=(40, 0))],
            [sg.Button("Remover Vacina no Animal Escolhido", key='3', size=(40, 0))],
            [sg.Button("Listar Vacinas Aplicadas no Animal Escolhido", key='4', size=(40, 0))],
            [sg.Button("Retornar", key='0', size=(40, 0))],
            [sg.Cancel('Cancelar', size=(40, 0))]
        ]
        self.__janela = sg.Window("ONG Lar de Cachorros e Gatos").layout(tela_opcoes)

    def pega_dados_vacina(self, dados_vacina_editar = {"nome_vacina": "", "ano_vacina": "", "mes_vacina": "", "dia_vacina": ""}):

        nome_vacina = dados_vacina_editar['nome_vacina']
        ano_vacina = dados_vacina_editar['ano_vacina']
        mes_vacina = dados_vacina_editar['mes_vacina']
        dia_vacina = dados_vacina_editar['dia_vacina']

        while True:
            sg.theme("DarkGreen")
            lista = ["raiva", "leptospirose", "hepatite infecciosa"]
            layout = [
                [sg.Text('Nome da Vacina:', size=(15, 1)), sg.Combo(lista,nome_vacina, key='nome_vacina')],
                [sg.Text('Ano:', size=(15, 1)), sg.InputText(ano_vacina, key='ano_vacina')],
                [sg.Text('Mês:', size=(15, 1)), sg.Combo([n + 1 for n in range(12)], default_value=mes_vacina, key='mes_vacina')],
                [sg.Text('Dia:', size=(15, 1)), sg.Combo([n + 1 for n in range(31)], default_value=dia_vacina, key='dia_vacina')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]

            self.__janela = sg.Window('Cadastrar Vacinas').Layout(layout)

            botao, valores = self.abre_janela()
            nome_vacina = valores['nome_vacina']
            ano_vacina = valores['ano_vacina']
            mes_vacina = valores['mes_vacina']
            dia_vacina = valores['dia_vacina']

            self.fechar()
            if botao == 'Cancelar':
                break

            data_vacina = None
            dados_validos = True
            if self.valida_ano(ano_vacina, mensagem_erro="Entrada não aceita! Ano Incoreto"):
                ano_vacina = int(ano_vacina)
                data_vacina = date(year=int(ano_vacina), month=int(mes_vacina), day=int(dia_vacina))
            else:
                dados_validos = False

            if dados_validos:
                break

        return {"nome_vacina": nome_vacina, "data_vacina": data_vacina, "ano_vacina": ano_vacina,
                "mes_vacina": mes_vacina, "dia_vacina": dia_vacina, "opcao": botao}

    def mostra_adocao(self, lista):
        sg.set_options(font=("Arial Bold", 14))
        cabecalho = ['Data da Vacina', 'Nome da Vacina']
        valores = []
        for vacina in lista:
            valores.append([
                str(vacina['data_vacina']),
                str(vacina['nome_vacina']),
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
        self.__janela = sg.Window("Mostrar vacina", layout, size=(1000, 700), resizable=True)
        self.__janela.read()

    def seleciona_vacina(self):
        nome_vacina = None
        lista = ["raiva", "leptospirose", "hepatite infecciosa"]
        while True:
            sg.theme("DarkGreen")
            layout = [
                [sg.Text('SELECIONAR VACINA')],
                [sg.Text('Escolha a vacina que deseja selecionar:')],
                [sg.Text('Nome da Vacina:', size=(15, 1)), sg.Combo(lista, nome_vacina, key='nome_vacina')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__janela = sg.Window('Seleciona Vacina').Layout(layout)

            botao, valores = self.abre_janela()
            self.fechar()
            if botao == 'Cancelar':
                break
            nome_vacina = valores["nome_vacina"]
            break
        return nome_vacina

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def abre_janela(self):
        botao, valores = self.__janela.read()
        return botao, valores