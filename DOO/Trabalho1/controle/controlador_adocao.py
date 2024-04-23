from entidade.adocao import Adocao
from limite.tela_adocao import TelaAdocao
from datetime import date
from entidade.adotante import Adotante


class ControladorAdocao:
    def __init__(self, controlador_sistema):
        self.__registros_adocao = []
        self.__tela_adocao = TelaAdocao()
        self.__controlador_sistema = controlador_sistema

    @property
    def registros_adocao(self):
        return self.__registros_adocao

    def pega_adocao_por_adotante(self, cpf: int):
        for adocao in self.__registros_adocao:
            if adocao.adotante.cpf == cpf:
                return adocao
            else:
                return None

    def cadastrar_adocao(self):
        self.__controlador_sistema.controlador_adotantes.listar_adotante()
        self.__controlador_sistema.controlador_cachorros.\
            listar_cachorro_disponiveis()
        self.__controlador_sistema.controlador_gatos.listar_gato_disponiveis()
        dados_adocao = self.__tela_adocao.pega_dados_adocao()

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
        adocao = Adocao(data, animal, adotante, termo_responsabilidade)
        self.__registros_adocao.append(adocao)
        self.__tela_adocao.mostra_mensagem("Adoção realizada com sucesso.")

    def editar_adocao(self):
        self.listar_adocao(self.__registros_adocao)
        cpf_adotante = self.__tela_adocao.seleciona_adocao()
        adocao = self.pega_adocao_por_adotante(cpf_adotante)

        try:
            if adocao is not None:
                self.__registros_adocao.remove(adocao)
                novos_dados_adocao = self.__tela_adocao.pega_dados_adocao()
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
                termo_responsabilidade = \
                    novos_dados_adocao["termo_responsabilidade"]
                adocao = Adocao(data_adocao, animal, adotante,
                                termo_responsabilidade)
                self.__tela_adocao.mostra_mensagem("Adocao alterada "
                                                   "com sucesso.")
                self.__registros_adocao.append(adocao)
            else:
                raise ValueError
        except ValueError:
            self.__tela_adocao.mostra_mensagem("ERRO: Adoção não existe!.")

    def listar_todas_adocoes(self):
        try:
            if self.__registros_adocao is not None:
                self.listar_adocao(self.__registros_adocao)
            else:
                raise ValueError
        except ValueError:
            self.__tela_adocao.mostra_mensagem("Nenhuma adoção foi "
                                               "registrada por enquanto")

    def listar_adocao(self, lista):
        for adocao in lista:
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

    def remover_adocao(self):
        self.listar_adocao(self.__registros_adocao)
        cpf_adotante = self.__tela_adocao.seleciona_adocao()
        adocao = self.pega_adocao_por_adotante(cpf_adotante)

        try:
            if adocao is not None:
                self.__registros_adocao.remove(adocao)
                self.__tela_adocao.mostra_mensagem("Adocao removida"
                                                   " com sucesso.")
                self.listar_adocao(self.__registros_adocao)
            else:
                raise ValueError
        except ValueError:
            self.__tela_adocao.mostra_mensagem("ERRO: adoção não existe!.")

    def buscar_adocao(self):
        cpf_adotante = self.__tela_adocao.seleciona_adocao()
        adocao = self.pega_adocao_por_adotante(cpf_adotante)

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
        for adocao in self.__registros_adocao:
            if adocao.data_adocao < data_final and \
                    adocao.data_adocao > data_inicial:
                registro_relatorio.append(adocao)
        if registro_relatorio is not None:
            self.listar_adocao(registro_relatorio)
        else:
            self.__tela_adocao.mostra_mensagem("Nenhuma doação registrada no "
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
