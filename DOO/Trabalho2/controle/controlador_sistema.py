from limite.tela_sistema import TelaSistema
from controle.controlador_adotante import ControladorAdotante
from controle.controlador_gato import ControladorGato
from controle.controlador_doador import ControladorDoador
from controle.controlador_cachorro import ControladorCachorro
from controle.controlador_adocao import ControladorAdocao
from controle.controlador_doacao import ControladorDoacao
from controle.controlador_vacina import ControladorVacina


class ControladorSistema:
    def __init__(self):
        self.__controlador_adotante = ControladorAdotante(self)
        self.__controlador_doador = ControladorDoador(self)
        self.__controlador_cachorro = ControladorCachorro(self)
        self.__controlador_gato = ControladorGato(self)
        self.__controlador_adocao = ControladorAdocao(self)
        self.__controlador_doacao = ControladorDoacao(self)
        self.__controlador_vacina = ControladorVacina(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_adotantes(self):
        return self.__controlador_adotante

    @property
    def controlador_doadores(self):
        return self.__controlador_doador

    @property
    def controlador_cachorros(self):
        return self.__controlador_cachorro

    @property
    def controlador_gatos(self):
        return self.__controlador_gato

    @property
    def controlador_adocoes(self):
        return self.__controlador_adocao

    @property
    def controlador_doacoes(self):
        return self.__controlador_doacao

    @property
    def controlador_vacinas(self):
        return self.__controlador_vacina

    def inicia_sistema(self):
        self.abre_tela()

    def doacao(self):
        return self.__controlador_doacao.abre_tela_doacao()

    def adotantes(self):
        return self.__controlador_adotante.abre_tela_adotante()

    def doadores(self):
        return self.__controlador_doador.abre_tela_doador()

    def cachorros(self):
        return self.__controlador_cachorro.abre_tela_cachorro()

    def gatos(self):
        return self.__controlador_gato.abre_tela_gato()

    def adocoes(self):
        return self.__controlador_adocao.abre_tela_adocao()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.adocoes, 2: self.doacao, 3: self.adotantes,
                        4: self.doadores, 5: self.cachorros, 6: self.gatos,
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()