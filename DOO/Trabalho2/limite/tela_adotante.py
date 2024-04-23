import PySimpleGUI as sg
from limite.tela_abstrata import TelaAbstrata
from datetime import date


class TelaAdotante(TelaAbstrata):
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
            [sg.Button("Cadastrar Adotante", key='1', size=(30, 0))],
            [sg.Button("Editar Adotante", key='2', size=(30, 0))],
            [sg.Button("Remover Adotante", key='3', size=(30, 0))],
            [sg.Button("Listar Adotante", key='4', size=(30, 0))],
            [sg.Button("Retornar", key='0', size=(30, 0))],
            [sg.Cancel('Cancelar', size=(30, 0))]
        ]
        self.__janela = sg.Window("ONG Lar de Cachorros e Gatos").layout(tela_opcoes)

    def pega_dados_adotante(self, dados_adotante_editar = {"nome": "", "cpf": "", "endereco": "", "tipo_habitacao": "", "tamanho_residencia": "", "possui_animal": "", "ano": "", "mes": "", "dia": "",}):
        nome = dados_adotante_editar['nome']
        cpf = dados_adotante_editar['cpf']
        endereco = dados_adotante_editar['endereco']
        tipo_habitacao = dados_adotante_editar['tipo_habitacao']
        tamanho_residencia = dados_adotante_editar['tamanho_residencia']
        possui_animal = dados_adotante_editar['possui_animal']
        ano = dados_adotante_editar['ano']
        mes = dados_adotante_editar['mes']
        dia = dados_adotante_editar['dia']

        while True:
            sg.theme("DarkGreen")

            layout = [
                [sg.Text('Nome:', size=(15, 1)), sg.InputText(nome, key='nome')],
                [sg.Text('CPF:', size=(15, 1)), sg.InputText(cpf, key='cpf')],
                [sg.Text('Ano:', size=(15, 1)), sg.InputText(ano, key='ano')],
                [sg.Text('Mês:', size=(15, 1)), sg.Combo([n+1 for n in range(12)], default_value=mes, key='mes')],
                [sg.Text('Dia:', size=(15, 1)), sg.Combo([n+1 for n in range(31)], default_value=dia, key='dia')],
                [sg.Text('Endereço:', size=(15, 1)), sg.InputText(endereco, key='endereco')],
                [sg.Text('Tipo da habitação:', size=(15, 1)), sg.Combo(["casa", "apartamento"], default_value=tipo_habitacao, key='tipo_habitacao')],
                [sg.Text('Tamanho da residencia:', size=(15, 1)), sg.Combo(["pequeno", "medio", "grande"], default_value=tamanho_residencia, key='tamanho_residencia')],
                [sg.Text('Possui animal?:', size=(15, 1)), sg.Combo(["sim", "nao"], default_value=possui_animal, key='possui_animal')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]

            self.__janela = sg.Window('Cadastrar Adotante').Layout(layout)

            botao, valores = self.abre_janela()
            nome = valores['nome']
            cpf = valores['cpf']
            ano = valores['ano']
            mes = valores['mes']
            dia = valores['dia']
            data_nascimento = None
            endereco = valores['endereco']
            tipo_habitacao = valores['tipo_habitacao']
            tamanho_residencia = valores['tamanho_residencia']
            possui_animal = valores['possui_animal']

            self.fechar()
            if botao == 'Cancelar':
                break

            dados_validos = True
            if self.valida_num_strig(nome, mensagem_erro="Entrada não aceita! Nome Incorreto"):
                nome = str(nome)
            else:
                sg.PopupOK("Nome Incorreto, Tente Novamente")
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
                sg.PopupOK("Endereço Incorreto, Tente Novamenter")
                dados_validos = False
            if self.valida_habitacao(tipo_habitacao, mensagem_erro="Entrada não aceita! Habitação Incorreta"):
                tipo_habitacao = str(tipo_habitacao)
            else:
                dados_validos = False
            if self.valida_tamanho(tamanho_residencia, mensagem_erro="Entrada não aceita! Tamanho Incorreto"):
                tamanho_residencia = str(tamanho_residencia)
            else:
                dados_validos = False
            if self.valida_propriedade_animal(possui_animal, mensagem_erro="Entrada não aceita! Animaal Incorreto"):
                possui_animal = str(possui_animal)
            else:
                dados_validos = False
            if dados_validos:
                break

        return {"nome": nome, "cpf": cpf, "ano": ano, "mes": mes,
                "dia": dia, "data_nascimento": data_nascimento,
                "endereco": endereco, "tipo_habitacao": tipo_habitacao,
                "tamanho_residencia": tamanho_residencia,
                "possui_animal": possui_animal, "opcao": botao}

    def mostra_adotante(self, adotantes):
        sg.set_options(font=("Arial Bold", 14))
        cabecalho = ['Nome', 'CPF', 'Data de Nascimento', 'Endereço',
                     'Tipo da habitação', 'Tamanho da Residência', 'Possui Animal']
        valores = []
        for adotante in adotantes:
            valores.append([
                str(adotante['nome']),
                str(adotante['cpf']),
                str(adotante['data_nascimento']),
                str(adotante['endereco']),
                str(adotante['tipo_habitacao']),
                str(adotante['tamanho_residencia']),
                str(adotante['possui_animal'])
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
        self.__janela = sg.Window("Mostrar adotante", layout, size=(1000, 700), resizable=True)
        self.__janela.read()

    def seleciona_adotante(self):
        cpf = None
        while True:
            sg.theme("DarkGreen")
            layout = [
                [sg.Text('SELECIONAR ADOTANTE')],
                [sg.Text('Digite o Numero do CPF que deseja selecionar:')],
                [sg.Text('NUMERO DO CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__janela = sg.Window('Seleciona Adotante').Layout(layout)

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