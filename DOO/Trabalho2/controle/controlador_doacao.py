from entidade.doacao import Doacao
from limite.tela_doacao import TelaDoacao
from entidade.doador import Doador
from entidade.gato import Gato
from entidade.cachorro import Cachorro


class ControladorDoacao:
    def __init__(self, controlador_sistema):
        self.__registros_doacao = []
        self.__tela_doacao = TelaDoacao()
        self.__controlador_sistema = controlador_sistema

    @property
    def registros_doacao(self):
        return self.__registros_doacao

    def pega_doacao_por_doador(self, cpf: int):
        for doacao in self.__registros_doacao:
            if doacao.doador.cpf == cpf:
                return doacao
            else:
                return None

    def cadastrar_doacao(self):
        dados_doacao = self.__tela_doacao.pega_dados_doacao()
        doador = self.__controlador_sistema.controlador_doadores.\
            pega_doador_por_cpf(dados_doacao["cpf"])
        doador = self.valida_doador(doador)
        tipo_animal = dados_doacao["animal_doado"]
        if tipo_animal == "G":
            animal = self.__controlador_sistema.controlador_gatos.\
                pega_gato_por_chip(dados_doacao["numero_chip"])
            animal = self.valida_gato(animal)
        else:
            animal = self.__controlador_sistema.controlador_cachorros.\
                pega_cachorro_por_chip(dados_doacao["numero_chip"])
            animal = self.valida_cachorro(animal)
        data_doacao = dados_doacao["data_doacao"]
        motivo_doacao = dados_doacao["motivo_doacao"]
        doacao = Doacao(data_doacao, animal, doador, motivo_doacao)
        self.__registros_doacao.append(doacao)
        self.__tela_doacao.mostra_mensagem("Doação realizada com sucesso.")

    def editar_doacao(self):
        self.listar_doacao(self.__registros_doacao)
        cpf_doador = self.__tela_doacao.seleciona_doacao()
        doacao = self.pega_doacao_por_doador(cpf_doador)

        try:
            if doacao is not None:
                self.__registros_doacao.remove(doacao)
                novos_dados_doacao = self.__tela_doacao.pega_dados_doacao()
                doador = self.__controlador_sistema.controlador_doadores.\
                    pega_doador_por_cpf(novos_dados_doacao["cpf"])
                doador = self.valida_doador(doador)
                tipo_animal = novos_dados_doacao["animal_doado"]
                if tipo_animal == "G":
                    animal = self.__controlador_sistema.controlador_gatos.\
                        pega_gato_por_chip(novos_dados_doacao["numero_chip"])
                    animal = self.valida_gato(animal)
                elif tipo_animal == "C":
                    animal = self.__controlador_sistema.controlador_cachorros.\
                        pega_cachorro_por_chip(novos_dados_doacao
                                               ["numero_chip"])
                    animal = self.valida_cachorro(animal)
                data_doacao = novos_dados_doacao["data_doacao"]
                motivo_doacao = novos_dados_doacao["motivo_doacao"]
                doacao = Doacao(data_doacao, animal, doador, motivo_doacao)
                self.__tela_doacao.mostra_mensagem("Doação alterada "
                                                   "com sucesso.")
                self.mostra_doacao(doacao)
                self.__registros_doacao.append(doacao)
            else:
                raise ValueError
        except ValueError:
            self.__tela_doacao.mostra_mensagem("ERRO: Doação não existe!.")

    def listar_todas_doacoes(self):
        try:
            if self.__registros_doacao is not None:
                self.listar_doacao(self.__registros_doacao)
            else:
                raise ValueError
        except ValueError:
            self.__tela_doacao.mostra_mensagem("Nenhuma doacao foi "
                                               "registrada por enquanto")

    def listar_doacao(self, lista):
        for doacao in lista:
            self.__tela_doacao.mostra_doacao({"data_doacao":
                                             doacao.data_doacao,
                                              "motivo_doacao":
                                             doacao.motivo_doacao})
            doador = doacao.doador
            self.__controlador_sistema.controlador_doadores.\
                pedir_mostra_doador(doador)
            animal = doacao.animal
            tipo_animal = doacao.animal.numero_chip
            tipo_animal = tipo_animal[0]
            if tipo_animal == "G":
                self.__controlador_sistema.controlador_gatos.\
                    pedir_mostra_gato(animal)
            elif tipo_animal == "C":
                self.__controlador_sistema.controlador_cachorros.\
                    pedir_mostra_cachorro(animal)

    def remover_doacao(self):
        self.listar_doacao(self.__registros_doacao)
        cpf_doador = self.__tela_doacao.seleciona_doacao()
        doacao = self.pega_doacao_por_doador(cpf_doador)

        try:
            if doacao is not None:
                self.__registros_doacao.remove(doacao)
                self.__tela_doacao.mostra_mensagem("Doação removida "
                                                   "com sucesso.")
                self.listar_doacao(self.__registros_doacao)
            else:
                raise ValueError
        except ValueError:
            self.__tela_doacao.mostra_mensagem("ERRO: Doação não existe!.")

    def relatorios_doacao(self):
        registro_relatorio = []
        data_inicial, data_final = self.__tela_doacao.pega_data_relatorio()
        for doacao in self.__registros_doacao:
            if doacao.data_doacao < data_final and \
                    doacao.data_doacao > data_inicial:
                registro_relatorio.append(doacao)
        if registro_relatorio is not None:
            self.listar_doacao(registro_relatorio)
        else:
            self.__tela_doacao.mostra_mensagem("Nenhuma doação registrada no"
                                               " intervalo de tempo escolhido")

    def mostra_doacao(self, doacao: Doacao):
        self.__tela_doacao.mostra_doacao({"data_doacao": doacao.data_doacao,
                                          "motivo_doacao":
                                              doacao.motivo_doacao})
        doador = doacao.doador
        self.__controlador_sistema.controlador_doadores.\
            pedir_mostra_doador(doador)
        animal = doacao.animal
        tipo_animal = doacao.animal.numero_chip
        tipo_animal = tipo_animal[0]
        if tipo_animal == "G":
            self.__controlador_sistema.controlador_gatos.\
                pedir_mostra_gato(animal)
        elif tipo_animal == "C":
            self.__controlador_sistema.controlador_cachorros.\
                pedir_mostra_cachorro(animal)

    def valida_doador(self, doador):
        try:
            if not (isinstance(doador, Doador)):
                raise ValueError
            else:
                return doador
        except ValueError:
            self.__tela_doacao.mostra_mensagem("Doador repassado não existe")
            self.abre_tela_doacao()

    def valida_gato(self, gato):
        try:
            if not (isinstance(gato, Gato)):
                raise ValueError
            else:
                return gato
        except ValueError:
            self.__tela_doacao.mostra_mensagem("Gato repassado não existe")
            self.abre_tela_doacao()

    def valida_cachorro(self, cachorro):
        try:
            if not (isinstance(cachorro, Cachorro)):
                raise ValueError
            else:
                return cachorro
        except ValueError:
            self.__tela_doacao.mostra_mensagem("Cachorro repassado não existe")
            self.abre_tela_doacao()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela_doacao(self):
        lista_opcoes = {1: self.cadastrar_doacao, 2: self.editar_doacao,
                        3: self.remover_doacao, 4: self.listar_todas_doacoes,
                        5: self.relatorios_doacao,
                        0: self.retornar}

        while True:
            lista_opcoes[self.__tela_doacao.tela_opcoes()]()