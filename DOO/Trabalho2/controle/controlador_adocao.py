from entidade.adocao import Adocao
from limite.tela_adocao import TelaAdocao
from datetime import date
from entidade.adotante import Adotante
from persistencia.adocao_dao import AdocaoDAO


class ControladorAdocao:
    def __init__(self, controlador_sistema):
        self.__adocao_dao = AdocaoDAO()
        self.__tela_adocao = TelaAdocao()
        self.__controlador_sistema = controlador_sistema

    @property
    def registros_adocao(self):
        return self.__adocao_dao.pega_todos()

    def pega_adocao_por_codigo(self, codigo_adocao: int):
        for adocao in self.__adocao_dao.pega_todos():
            if adocao.codigo_adocao == codigo_adocao:
                return adocao
            else:
                return None

    def cadastrar_adocao(self):
        self.__controlador_sistema.controlador_adotantes.listar_adotante()
        self.__controlador_sistema.controlador_cachorros.\
            listar_cachorro_disponiveis()
        self.__controlador_sistema.controlador_gatos.listar_gato_disponiveis()
        dados_adocao = self.__tela_adocao.pega_dados_adocao()
        if dados_adocao["opcao"] == 'Confirmar':
            adotante = self.__controlador_sistema.controlador_adotantes.\
                pega_adotante_por_cpf(dados_adocao["cpf"])
            self.valida_adotante_idade(adotante)
            tipo_animal = dados_adocao["animal_adotado"]
            if tipo_animal == "G":
                animal = self.__controlador_sistema.controlador_gatos.\
                    pega_gato_por_chip(dados_adocao["numero_chip"])
            else:
                animal = self.__controlador_sistema.controlador_cachorros.\
                    pega_cachorro_por_chip(dados_adocao["numero_chip"])
                self.valida_adotante_casa(adotante, animal)
            data = dados_adocao["data_adocao"]
            termo_responsabilidade = dados_adocao["termo_responsabilidade"]
            codigo_adocao = dados_adocao["codigo_adocao"]
            adocao = Adocao(data, animal, adotante, termo_responsabilidade, codigo_adocao)
            self.__adocao_dao.adiciona(adocao)
            self.__tela_adocao.mostra_mensagem("Adoção realizada com sucesso.")

    def editar_adocao(self):
        self.listar_adocao()
        codigo_adocao = self.__tela_adocao.seleciona_adocao()
        if codigo_adocao is not None:
            adocao = self.pega_adocao_por_codigo(codigo_adocao)

            try:
                if adocao is not None:
                    self.__adocao_dao.remove(codigo_adocao)
                    novos_dados_adocao = self.__tela_adocao.pega_dados_adocao({"ano": adocao.ano.year, "mes": adocao.mes.month, "dia": adocao.dia.day,
                                                                               "data_adocao": adocao.data_adocao, "numero_chip": adocao.animal.numero_chip,
                                                                               "animal_adotado": adocao.animal_adotado,"termo_responsabilidade":
                                                                                   adocao.termo_responsabilidade, "codigo_adocao": adocao.codigo_adocao,
                                                                               "cpf": adocao.adotante.cpf})
                    adotante = self.__controlador_sistema.controlador_adotantes. \
                        pega_adotante_por_cpf(novos_dados_adocao["cpf"])
                    self.valida_adotante_idade(adotante)
                    self.valida_adotante_se_doou(adotante)
                    tipo_animal = novos_dados_adocao["animal_adotado"]
                    if tipo_animal == "G":
                        animal = self.__controlador_sistema.controlador_gatos. \
                            pega_gato_por_chip(novos_dados_adocao["numero_chip"])
                    elif tipo_animal == "C":
                        animal = self.__controlador_sistema.controlador_cachorros. \
                            pega_cachorro_por_chip(novos_dados_adocao
                                                   ["numero_chip"])
                        self.valida_adotante_casa(adotante, animal)
                    data_adocao = novos_dados_adocao["data_adocao"]
                    codigo_adocao = novos_dados_adocao["codigo_adocao"]
                    termo_responsabilidade = \
                        novos_dados_adocao["termo_responsabilidade"]
                    adocao = Adocao(data_adocao, animal, adotante,
                                    termo_responsabilidade, codigo_adocao)
                    self.__tela_adocao.mostra_mensagem("Adocao alterada "
                                                       "com sucesso.")
                    self.__adocao_dao.adiciona(adocao)
                else:
                    raise ValueError
            except ValueError:
                self.__tela_adocao.mostra_mensagem("ERRO: Adoção não existe!.")

    def listar_todas_adocoes(self):
        try:
            if self.__adocao_dao is not None:
                self.listar_adocao()
            else:
                raise ValueError
        except ValueError:
            self.__tela_adocao.mostra_mensagem("Nenhuma adoção foi "
                                               "registrada por enquanto")

    def listar_adocao(self):
        lista = []
        for adocao in self.__adocao_dao.pega_todos():
            lista.append({"data_adocao": adocao.data, "nome_adotante": adocao.adotante.nome,
                          "termo_responsabilidade": adocao.termo_responsabilidade,
                          "numero_chip": adocao.animal.numero_chip, "codigo_adocao": adocao.codigo_adocao})
            adotante = adocao.adotante
            self.__controlador_sistema.controlador_adotantes.\
                pedir_mostra_adotante(adotante)
            animal = adocao.animal
            tipo_animal = adocao.animal.numero_chip
            tipo_animal = tipo_animal[0]
            # if tipo_animal == "G":
            #     self.__controlador_sistema.controlador_gatos.\
            #         pedir_mostra_gato(animal)
            # elif tipo_animal == "C":
            #     self.__controlador_sistema.controlador_cachorros.\
            #         pedir_mostra_cachorro(animal)


        self.__tela_adocao.mostra_adocao(lista)

    def remover_adocao(self):
        self.listar_adocao()
        codigo_adocao = self.__tela_adocao.seleciona_adocao()
        adocao = self.pega_adocao_por_codigo(codigo_adocao)

        try:
            if adocao is not None:
                self.__adocao_dao.remove(codigo_adocao)
                self.__tela_adocao.mostra_mensagem("Adocao removida"
                                                   " com sucesso.")
                self.listar_adocao()
            else:
                raise ValueError
        except ValueError:
            self.__tela_adocao.mostra_mensagem("ERRO: adoção não existe!.")

    def buscar_adocao(self):
        codigo_adocao = self.__tela_adocao.seleciona_adocao()
        adocao = self.pega_adocao_por_codigo(codigo_adocao)

        try:
            if adocao is not None:
                self.mostra_adocao(adocao)
            else:
                raise ValueError
        except ValueError:
            self.__tela_adocao.mostra_mensagem("ERRO: adoção não existe!.")

    def mostra_adocao(self, adocao: Adocao):
        self.__tela_adocao.mostra_adocao({"data_adocao": adocao.data,
                                          "termo_responsabilidade":
                                          adocao.termo_responsabilidade})
        adotante = adocao.adotante
        self.__controlador_sistema.controlador_adotantes.\
            pedir_mostra_adotante(adotante)
        animal = adocao.animal
        tipo_animal = adocao.animal.numero_chip
        tipo_animal = tipo_animal[0]
        if tipo_animal == "G":
            self.__controlador_sistema.controlador_gatos.\
                pedir_mostra_gato(animal)
        elif tipo_animal == "C":
            self.__controlador_sistema.controlador_cachorros.\
                pedir_mostra_cachorro(animal)

    def relatorios_adocao(self):
        registro_relatorio = []
        data_inicial, data_final = self.__tela_adocao.pega_data_relatorio()
        for adocao in self.__adocao_dao.pega_todos():
            if adocao.data < data_final and \
                    adocao.data > data_inicial:
                registro_relatorio.append(adocao)
        if registro_relatorio is not None:
            self.listar_adocao(registro_relatorio)
        else:
            self.__tela_adocao.mostra_mensagem("Nenhuma adoção registrada no "
                                               "intervalo de tempo escolhido")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def valida_adotante_idade(self, adotante):
        try:
            if isinstance(adotante, Adotante):
                data = date.today()
                data_adotante = adotante.data_nascimento
                diferenca_ano = data.year - data_adotante.year
                diferenca_mes = data.month - data_adotante.month
                diferenca_dia = data.day - data_adotante.day
                if diferenca_ano < 18:
                    raise ValueError
                elif diferenca_ano == 18:
                    if diferenca_mes < 0:
                        raise ValueError
                    elif diferenca_mes == 0:
                        if diferenca_dia < 0:
                            raise ValueError
        except ValueError:
            self.__tela_adocao.mostra_mensagem("O adotante escolhido não pode"
                                               " adotar, menor de 18 anos")
            self.abre_tela_adocao()

    def valida_adotante_casa(self, adotante, cachorro):
        try:
            if cachorro.tamanho == "GRANDE":
                if adotante.tipo_habitacao == "APARTAMENTO":
                    if adotante.tamanho_residencia == "PEQUENO":
                        raise ValueError
        except ValueError:
            self.__tela_adocao.mostra_mensagem("Adoção não aceita pois animal "
                                               "muito grande para um "
                                               "apartamento pequeno")
            self.abre_tela_adocao()

    def valida_adotante_se_doou(self, adotante):
        try:
            for doacao in self.__controlador_sistema.controlador_doacoes.\
                    registros_doacao:
                if doacao.doador.cpf == adotante.cpf:
                    raise ValueError
        except ValueError:
            self.__tela_adocao.mostra_mensagem("Adotante não pode adotar por "
                                               "que já doou algum animal para"
                                               " essa mesma ONG")

    def abre_tela_adocao(self):
        lista_opcoes = {1: self.cadastrar_adocao, 2: self.editar_adocao,
                        3: self.remover_adocao, 4: self.listar_todas_adocoes,
                        5: self.buscar_adocao, 6: self.relatorios_adocao,
                        0: self.retornar}

        while True:
            lista_opcoes[self.__tela_adocao.tela_opcoes()]()