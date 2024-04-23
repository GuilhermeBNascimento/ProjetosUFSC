from entidade.cachorro import Cachorro
from limite.tela_cachorro import TelaCachorro


class ControladorCachorro:
    def __init__(self, controlador_sistema):
        self.__cachorros = []
        self.__cachorros_disponiveis = []
        self.__tela_cachorro = TelaCachorro()
        self.__controlador_sistema = controlador_sistema

    @property
    def cachorros(self):
        return self.__cachorros

    @property
    def cachorros_disponiveis(self):
        return self.__cachorros_disponiveis

    def pega_cachorro_por_chip(self, numero_chip: int):
        for cachorro in self.__cachorros:
            if cachorro.numero_chip == numero_chip:
                return cachorro
            else:
                return None

    def cadastrar_cachorro(self):
        dados_cachorro = self.__tela_cachorro.pega_dados_cachorro()
        cachorro = self.pega_cachorro_por_chip(dados_cachorro["numero_chip"])

        try:
            if cachorro is None:
                cachorro = Cachorro(dados_cachorro["numero_chip"],
                                    dados_cachorro["nome"],
                                    dados_cachorro["raca"],
                                    dados_cachorro["tamanho"])
                self.__cachorros.append(cachorro)
                self.__cachorros_disponiveis.append(cachorro)
                self.__tela_cachorro.mostra_mensagem("Cachorro adicionado"
                                                     " com sucesso.")
            else:
                raise ValueError
        except ValueError:
            self.__tela_cachorro.mostra_mensagem("ERRO: Cachorro já existe!.")

    def editar_cachorro(self):
        self.listar_cachorro()
        numero_chip = self.__tela_cachorro.seleciona_cachorro()
        cachorro = self.pega_cachorro_por_chip(numero_chip)

        try:
            if cachorro is not None:
                self.checa_cachorro(cachorro)
                if cachorro in self.__cachorros_disponiveis:
                    self.__cachorros_disponiveis.remove(cachorro)
                novos_dados_cachorro = self.__tela_cachorro.\
                    pega_dados_cachorro()
                cachorro.numero_chip = novos_dados_cachorro["numero_chip"]
                cachorro.nome = novos_dados_cachorro["nome"]
                cachorro.raca = novos_dados_cachorro["raca"]
                cachorro.tamanho = novos_dados_cachorro["tamanho"]
                self.__tela_cachorro.mostra_mensagem("Cachorro alterado "
                                                     "com sucesso.")
                self.__cachorros_disponiveis.append(cachorro)
                self.listar_cachorro()
            else:
                raise ValueError
        except ValueError:
            self.__tela_cachorro.mostra_mensagem("ERRO: Cachorro não existe!.")

    def listar_cachorro(self):
        for cachorro in self.__cachorros:
            self.__tela_cachorro.mostra_cachorro({"numero_chip":
                                                  cachorro.numero_chip,
                                                  "nome": cachorro.nome,
                                                  "raca": cachorro.raca,
                                                  "tamanho": cachorro.tamanho})

    def listar_cachorro_disponiveis(self):
        for cachorro in self.__cachorros_disponiveis:
            vacina1 = "raiva"
            vacina2 = "leptospirose"
            vacina3 = "hepatite infecciosa"
            cont = int(0)
            for vacina in cachorro.vacinas:
                if vacina.nome_vacina == vacina1:
                    cont = cont + 1
                    if cont == 3:
                        self.pedir_mostra_cachorro(cachorro)
                elif vacina.nome_vacina == vacina2:
                    cont = cont + 1
                    if cont == 3:
                        self.pedir_mostra_cachorro(cachorro)
                elif vacina.nome_vacina == vacina3:
                    cont = cont + 1
                    if cont == 3:
                        self.pedir_mostra_cachorro(cachorro)

    def remover_cachorro(self):
        self.listar_cachorro()
        numero_chip = self.__tela_cachorro.seleciona_cachorro()
        cachorro = self.pega_cachorro_por_chip(numero_chip)

        try:
            if cachorro is not None:
                self.checa_cachorro(cachorro)
                self.__cachorros.remove(cachorro)
                if cachorro in self.__cachorros_disponiveis:
                    self.__cachorros_disponiveis.remove(cachorro)
                self.__tela_cachorro.mostra_mensagem("Cachorro removido "
                                                     "com sucesso.")
                self.listar_cachorro()
            else:
                raise ValueError
        except ValueError:
            self.__tela_cachorro.mostra_mensagem("ERRO: Cachorro não existe!.")

    def buscar_cachorro(self):
        num_chip_cachorro = self.__tela_cachorro.seleciona_cachorro()
        cachorro = self.pega_cachorro_por_chip(num_chip_cachorro)

        try:
            if cachorro is not None:
                self.__tela_cachorro.mostra_cachorro({"numero_chip":
                                                     cachorro.numero_chip,
                                                      "nome": cachorro.nome,
                                                      "raca": cachorro.raca,
                                                      "tamanho":
                                                     cachorro.tamanho})
            else:
                raise ValueError
        except ValueError:
            self.__tela_cachorro.mostra_mensagem("ERRO: Cachorro não existe!")

    def pedir_mostra_cachorro(self, cachorro: Cachorro):
        try:
            if cachorro is not None:
                self.__tela_cachorro.mostra_cachorro({"numero_chip":
                                                      cachorro.numero_chip,
                                                      "nome": cachorro.nome,
                                                      "raca": cachorro.raca,
                                                      "tamanho":
                                                      cachorro.tamanho})
            else:
                raise ValueError
        except ValueError:
            self.__tela_cachorro.mostra_mensagem("ERRO: Cachorro "
                                                 "não foi repassado")

    def vacinas(self):
        num_chip_cachorro = self.__tela_cachorro.seleciona_cachorro()
        cachorro = self.pega_cachorro_por_chip(num_chip_cachorro)
        try:
            if cachorro is not None:
                self.__controlador_sistema.controlador_vacinas. \
                    abre_tela_vacina(cachorro)
            else:
                raise ValueError
        except ValueError:
            self.__tela_cachorro.mostra_mensagem("Esse cachorro não existe")

    def checa_cachorro(self, cachorro):
        try:
            for adocao in self.__controlador_sistema.\
                    controlador_adocoes.registros_adocao:
                if adocao.animal == cachorro:
                    raise ValueError
                else:
                    return cachorro
        except ValueError:
            self.__tela_cachorro.mostra_mensagem("Cachorro não pode ser "
                                                 "excluido ou editado por que"
                                                 " já foi adotado, a adocao "
                                                 "tem que ser excluida "
                                                 "primeiro.")
            self.abre_tela_cachorro()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela_cachorro(self):
        lista_opcoes = {1: self.cadastrar_cachorro, 2: self.editar_cachorro,
                        3: self.remover_cachorro, 4: self.listar_cachorro,
                        5: self.buscar_cachorro, 6: self.vacinas,
                        7: self.listar_cachorro_disponiveis, 0: self.retornar}

        while True:
            lista_opcoes[self.__tela_cachorro.tela_opcoes()]()
