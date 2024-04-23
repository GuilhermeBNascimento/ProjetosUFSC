from entidade.gato import Gato
from limite.tela_gato import TelaGato
from persistencia.gato_dao import GatoDAO


class ControladorGato:
    def __init__(self, controlador_sistema):
        self.__gato_dao = GatoDAO()
        self.__gatos_disponiveis = []
        self.__tela_gato = TelaGato()
        self.__controlador_sistema = controlador_sistema

    @property
    def gatos(self):
        return self.__gato_dao.pega_todos()

    @property
    def gatos_disponiveis(self):
        return self.__gatos_disponiveis

    def pega_gato_por_chip(self, numero_chip: str):
        for gato in self.__gato_dao.pega_todos():
            if gato.numero_chip == numero_chip:
                return gato
            else:
                return None

    def cadastrar_gato(self):
        dados_gato = self.__tela_gato.pega_dados_gato()
        if dados_gato["opcao"] == 'Confirmar':
            gato = self.pega_gato_por_chip(dados_gato["numero_chip"])

            try:
                if gato is None:
                    gato = Gato(dados_gato["numero_chip"], dados_gato["nome"],
                                dados_gato["raca"], dados_gato["cor_pelo"])
                    self.__gato_dao.adiciona(gato)
                    self.__gatos_disponiveis.append(gato)
                    self.__tela_gato.mostra_mensagem("Gato adicionado"
                                                     " com sucesso.")
                else:
                    raise ValueError
            except ValueError:
                self.__tela_gato.mostra_mensagem("ERRO: Gato já existe!.")

    def editar_gato(self):
        self.listar_gato()
        numero_chip = self.__tela_gato.seleciona_gato()
        if numero_chip is not None:
            gato = self.pega_gato_por_chip(numero_chip)

            try:
                if gato is not None:
                    self.checa_gato(gato)
                    novos_dados_gato = self.__tela_gato.pega_dados_gato({"numero_chip": gato.numero_chip, "nome": gato.nome, "raca": gato.raca, "cor_pelo": gato.cor_pelo})
                    gato.numero_chip = novos_dados_gato["numero_chip"]
                    gato.nome = novos_dados_gato["nome"]
                    gato.raca = novos_dados_gato["raca"]
                    gato.cor_pelo = novos_dados_gato["cor_pelo"]
                    self.__tela_gato.mostra_mensagem("Gato alterado com sucesso.")
                    self.listar_gato()
                else:
                    raise ValueError
            except ValueError:
                self.__tela_gato.mostra_mensagem("ERRO: Gato não existe!.")

    def listar_gato(self):
        gatos = []
        for gato in self.__gato_dao.pega_todos():
            gatos.append({"numero_chip": gato.numero_chip,
                                          "nome": gato.nome, "raca": gato.raca,
                                          "cor_pelo": gato.cor_pelo})
        self.__tela_gato.mostra_gato(gatos)

    def listar_gato_disponiveis(self):
        for gato in self.__gatos_disponiveis:
            vacina1 = "raiva"
            vacina2 = "leptospirose"
            vacina3 = "hepatite infecciosa"
            cont = int(0)
            for vacina in gato.vacinas:
                if vacina.nome_vacina == vacina1:
                    cont = cont + 1
                    if cont == 3:
                        self.pedir_mostra_gato(gato)
                elif vacina.nome_vacina == vacina2:
                    cont = cont + 1
                    if cont == 3:
                        self.pedir_mostra_gato(gato)
                elif vacina.nome_vacina == vacina3:
                    cont = cont + 1
                    if cont == 3:
                        self.pedir_mostra_gato(gato)

    def remover_gato(self):
        self.listar_gato()
        numero_chip = self.__tela_gato.seleciona_gato()
        gato = self.pega_gato_por_chip(numero_chip)

        try:
            if gato is not None:
                self.checa_gato(gato)
                self.__gato_dao.remove(numero_chip)
                self.__tela_gato.mostra_mensagem("Gato removido com sucesso.")
                self.listar_gato()
            else:
                raise ValueError
        except ValueError:
            self.__tela_gato.mostra_mensagem("ERRO: Gato não existe!.")

    def buscar_gato(self):
        num_chip_gato = self.__tela_gato.seleciona_gato()
        gato = self.pega_gato_por_chip(num_chip_gato)

        try:
            if gato is not None:
                self.__tela_gato.mostra_gato({"numero_chip": gato.numero_chip,
                                              "nome": gato.nome,
                                              "raca": gato.raca,
                                              "cor_pelo": gato.cor_pelo})
            else:
                raise ValueError
        except ValueError:
            self.__tela_gato.mostra_mensagem("ERRO: Gato não existe!")

    def pedir_mostra_gato(self, gato: Gato):
        try:
            if gato is not None:
                self.__tela_gato.mostra_gato({"numero_chip": gato.numero_chip,
                                              "nome": gato.nome,
                                              "raca": gato.raca,
                                              "cor_pelo": gato.cor_pelo})
            else:
                raise ValueError
        except ValueError:
            self.__tela_gato.mostra_mensagem("ERRO: Gato não foi repassado")

    def vacinas(self):
        num_chip_gato = self.__tela_gato.seleciona_gato()
        gato = self.pega_gato_por_chip(num_chip_gato)
        try:
            if gato is not None:
                self.__controlador_sistema.controlador_vacinas.\
                    abre_tela_vacina(gato)
            else:
                raise ValueError
        except ValueError:
            self.__tela_gato.mostra_mensagem("Esse gato não existe")

    def checa_gato(self, gato):
        try:
            for adocao in self.__controlador_sistema.\
                    controlador_adocoes.registros_adocao:
                if adocao.animal == gato:
                    raise ValueError
                else:
                    return gato
        except ValueError:
            self.__tela_gato.mostra_mensagem("Gato não pode ser excluido "
                                             "ou editado por que já foi "
                                             "adotado, a adocao tem que ser "
                                             "excluida primeiro.")
            self.abre_tela_gato()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela_gato(self):
        lista_opcoes = {1: self.cadastrar_gato, 2: self.editar_gato,
                        3: self.remover_gato, 4: self.listar_gato,
                        5: self.vacinas, 6: self.__gatos_disponiveis,
                        0: self.retornar}

        while True:
            lista_opcoes[self.__tela_gato.tela_opcoes()]()