import PySimpleGUI as sg
from limite.tela_abstrata import TelaAbstrata
from datetime import date


class TelaAdocao(TelaAbstrata):
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
            [sg.Button("Cadastrar Adoção", key='1', size=(30, 0))],
            [sg.Button("Editar Adoção", key='2', size=(30, 0))],
            [sg.Button("Remover Adoção", key='3', size=(30, 0))],
            [sg.Button("Listar Adoção", key='4', size=(30, 0))],
            [sg.Button("Relatório de adoçôes por data", key='5', size=(30, 0))],
            [sg.Button("Retornar", key='0', size=(30, 0))],
            [sg.Cancel('Cancelar', size=(30, 0))]
        ]
        self.__janela = sg.Window("ONG Lar de Cachorros e Gatos").layout(tela_opcoes)

    def pega_dados_adocao(self, dados_adocao_editar={"ano": "", "mes": "", "dia": "", "numero_chip": "", "animal_adotado": "", "termo_responsabilidade": "", "cpf": "", "codigo_adocao": "", "nome": ""}):
        ano = dados_adocao_editar['ano']
        mes = dados_adocao_editar['mes']
        dia = dados_adocao_editar['dia']
        numero_chip = dados_adocao_editar['numero_chip']
        animal_adotado = dados_adocao_editar['animal_adotado']
        termo_responsabilidade = dados_adocao_editar['termo_responsabilidade']
        cpf = dados_adocao_editar['cpf']
        codigo_adocao = dados_adocao_editar['codigo_adocao']
        nome = dados_adocao_editar['nome']

        while True:
            sg.theme("DarkGreen")

            layout = [
                [sg.Text('Ano:', size=(15, 1)), sg.InputText(ano, key='ano')],
                [sg.Text('Mês:', size=(15, 1)), sg.Combo([n+1 for n in range(12)], default_value=mes, key='mes')],
                [sg.Text('Dia:', size=(15, 1)), sg.Combo([n+1 for n in range(31)], default_value=dia, key='dia')],
                [sg.Text('Numero do chip:', size=(15, 1)), sg.InputText(numero_chip, key='numero_chip')],
                [sg.Text("Nome Adotante:", size=(15, 1)), sg.InputText(nome, key='nome')],
                [sg.Text('Animal adotado:', size=(15, 1)), sg.Combo(["gato", "cachorro"], default_value=animal_adotado, key='animal_adotado')],
                [sg.Text('CPF Adotante:', size=(15, 1)), sg.InputText(cpf, key='cpf')],
                [sg.Text('Termo de responsabilidade:', size=(15, 1)), sg.Combo(["sim", "nao"], default_value=termo_responsabilidade, key='termo_responsabilidade')],
                [sg.Text("Codigo adoção: ", size=(15, 1)), sg.InputText(codigo_adocao, key='codigo_adocao')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]

            self.__janela = sg.Window('Cadastrar Adoção').Layout(layout)

            botao, valores = self.abre_janela()
            ano = valores['ano']
            mes = valores['mes']
            dia = valores['dia']
            data_adocao = None
            numero_chip = valores['numero_chip']
            animal_adotado = valores['animal_adotado']
            termo_responsabilidade = valores['termo_responsabilidade']
            nome = valores['nome']
            cpf = valores['cpf']
            codigo_adocao = valores['codigo_adocao']

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
                        data_adocao = date(year=int(ano), month=int(mes), day=int(dia))
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
            if self.valida_animal(animal_adotado, mensagem_erro="Entrada não aceita! Animal Incorreto"):
                animal_adotado = str(animal_adotado)
            else:
                dados_validos = False
            if self.termo_responsabilidade(termo_responsabilidade, mensagem_erro="Resposta incorreta!. Respostas Possíveis: SIM ou NÃO"):
                termo_responsabilidade = str(termo_responsabilidade)
            else:
                dados_validos = False
            if self.valida_inteiro(cpf, mensagem_erro="Entrada não aceita!. CPF Incorreto"):
                cpf = int(cpf)
            else:
                dados_validos = False
            if self.valida_inteiro(codigo_adocao, mensagem_erro="Entrada não aceita!. Codigo Incorreto"):
                codigo_adocao = int(codigo_adocao)
            else:
                dados_validos = False
            if self.valida_num_strig(nome,mensagem_erro="Entrada não aceita!. Codigo Incorreto"):
                nome = str(nome)
            else:
                dados_validos = False
            if dados_validos:
                break

        return {"ano": ano, "mes": mes, "dia": dia, "data_adocao": data_adocao,
                "numero_chip": numero_chip, "animal_adotado": animal_adotado,
                "termo_responsabilidade": termo_responsabilidade, "nome": nome,
                "cpf": cpf, "codigo_adocao": codigo_adocao, "opcao": botao}

    def mostra_adocao(self, lista):
        sg.set_options(font=("Arial Bold", 14))
        cabecalho = ['Data da Adoção', 'Numero do chip', 'Animal Adotado', 'Termo de Responsabilidade', 'Adotante',
                     'Animal', 'Codigo Adocao']
        valores = []
        for adocao in lista:
            valores.append([
                str(adocao['data_adocao']),
                str(adocao['animal_adotado']),
                str(adocao['termo_responsabilidade']),
                str(adocao['nome_adotante']),
                str(adocao['numero_chip']),
                str(adocao['codigo_adocao']),
                str(adocao['nome'])
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
        self.__janela = sg.Window("Mostrar adoção", layout, size=(1000, 700), resizable=True)
        self.__janela.read()

    def seleciona_adocao(self):
        codigo_adocao = None
        while True:
            sg.theme("DarkGreen")
            layout = [
                [sg.Text('SELECIONAR ADOCAO')],
                [sg.Text('Digite o codigo da adocao que deseja selecionar:')],
                [sg.Text('CODIGO DA ADOCAO:', size=(15, 1)), sg.InputText('', key='codigo_adocao')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__janela = sg.Window('Seleciona Adotante').Layout(layout)

            botao, valores = self.abre_janela()
            self.fechar()
            if botao == 'Cancelar':
                break
            codigo_adocao = valores["codigo_adocao"]

            if self.valida_inteiro(codigo_adocao, mensagem_erro="Codigo Incorreto"):
                codigo_adocao = int(codigo_adocao)
                break
        return codigo_adocao

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

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

    def abre_janela(self):
        botao, valores = self.__janela.read()
        return botao, valores