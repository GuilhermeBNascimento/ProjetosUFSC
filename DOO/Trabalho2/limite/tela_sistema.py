import PySimpleGUI as sg
from limite.tela_abstrata import TelaAbstrata


class TelaSistema(TelaAbstrata):
    def __init__(self):
        self.__janela = None
        self.inicia_componentes()

    def tela_opcoes(self):
        self.inicia_componentes()
        botao, valores = self.__janela.Read()
        if botao is None or botao in ['Cancelar', 'Finalizar Sistema']:
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

    def inicia_componentes(self):
        sg.theme('DarkGreen')
        tela_sistema = [
            [sg.Text("Amigos dos Pets ONG Lar de Cachorros e Gatos")],
            [sg.Text("Escolha sua opção")],
            [sg.Button("Registrar Adoção e Ler seus Relatórios", key='1', size=(30, 0))],
            [sg.Button("Registrar Doação e Ler seus Relatórios", key='2', size=(30, 0))],
            [sg.Button("Adotantes", key='3', size=(30, 0))],
            [sg.Button("Doadores", key='4', size=(30, 0))],
            [sg.Button("Cachorros", key='5', size=(30, 0))],
            [sg.Button("Gatos", key='6', size=(30, 0))],
            [sg.Button("Finalizar Sistema", key='0', size=(30, 0))],
            [sg.Cancel('Cancelar', key='Cancelar', size=(30, 0))]
        ]
        self.__janela = sg.Window("ONG Lar de Cachorros e Gatos").layout(tela_sistema)