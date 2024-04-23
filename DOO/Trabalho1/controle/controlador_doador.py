from entidade.doador import Doador
from limite.tela_doador import TelaDoador


class ControladorDoador:
    def __init__(self, controlador_sistema):
        self.__doadores = []
        self.__tela_doador = TelaDoador()
        self.__controlador_sistema = controlador_sistema

    @property
    def doadores(self):
        return self.__doadores

    def pega_doador_por_cpf(self, cpf: int):
        for doador in self.__doadores:
            if doador.cpf == cpf:
                return doador
            else:
                return None

    def cadastrar_doador(self):
        dados_doador = self.__tela_doador.pega_dados_doador()
        doador = self.pega_doador_por_cpf(dados_doador["cpf"])
        try:
            if doador is None:
                doador = Doador(dados_doador["nome"], dados_doador["cpf"],
                                dados_doador["data_nascimento"],
                                dados_doador["endereco"],
                                dados_doador["telefone"])
                self.__doadores.append(doador)
                self.__tela_doador.mostra_mensagem("Doador adicionado "
                                                   "com sucesso.")
            else:
                raise ValueError
        except ValueError:
            self.__tela_doador.mostra_mensagem("ERRO: Doador já existe!.")

    def editar_doador(self):
        self.listar_doador()
        cpf_doador = self.__tela_doador.seleciona_doador()
        doador = self.pega_doador_por_cpf(cpf_doador)
        self.checa_doador(doador)
        self.__doadores.remove(doador)
        novos_dados_doador = self.__tela_doador.pega_dados_doador()
        nome = novos_dados_doador["nome"]
        cpf = novos_dados_doador["cpf"]
        data_nascimento = novos_dados_doador["data_nascimento"]
        endereco = novos_dados_doador["endereco"]
        telefone = novos_dados_doador["telefone"]
        doador = Doador(nome, cpf, data_nascimento, endereco, telefone)
        self.__doadores.append(doador)
        self.__tela_doador.mostra_mensagem("Doador alterado "
                                           "com sucesso.")
        self.listar_doador()

    def listar_doador(self):
        for doador in self.__doadores:
            self.__tela_doador.mostra_doador({"nome": doador.nome, "cpf":
                                             doador.cpf, "data_nascimento":
                                             doador.data_nascimento,
                                             "endereco": doador.endereco,
                                              "telefone": doador.telefone})

    def remover_doador(self):
        self.listar_doador()
        self.__tela_doador.mostra_mensagem("CPF do Doador que queira remover:")
        cpf_doador = self.__tela_doador.seleciona_doador()
        doador = self.pega_doador_por_cpf(cpf_doador)

        try:
            if doador is not None and isinstance(doador, Doador):
                self.checa_doador(doador)
                self.__doadores.remove(doador)
                self.__tela_doador.mostra_mensagem("Doador removido"
                                                   " com sucesso.")
                self.listar_doador()
            else:
                raise ValueError
        except ValueError:
            self.__tela_doador.mostra_mensagem("ERRO: Doador não existe!.")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def buscar_doador(self):
        cpf_doador = self.__tela_doador.seleciona_doador()
        doador = self.pega_doador_por_cpf(cpf_doador)

        try:
            if doador is not None and isinstance(doador, Doador):
                self.__tela_doador.mostra_doador({"nome": doador.nome,
                                                  "cpf": doador.cpf,
                                                  "data_nascimento":
                                                  doador.data_nascimento,
                                                  "endereco": doador.endereco,
                                                  "telefone": doador.telefone})
            else:
                raise ValueError
        except ValueError:
            self.__tela_doador.mostra_mensagem("ERRO: Doador não existe!")

    def pedir_mostra_doador(self, doador: Doador):
        try:
            if doador is not None and isinstance(doador, Doador):
                self.__tela_doador.mostra_doador({"nome": doador.nome,
                                                  "cpf": doador.cpf,
                                                  "data_nascimento":
                                                  doador.data_nascimento,
                                                  "endereco": doador.endereco,
                                                  "telefone": doador.telefone})
            else:
                raise ValueError
        except ValueError:
            self.__tela_doador.mostra_mensagem("ERRO: Doador "
                                               "não foi repassado")

    def checa_doador(self, doador):
        try:
            for doacao in self.__controlador_sistema.controlador_doacoes.\
                    registros_doacao:
                if doacao.doador == doador:
                    raise ValueError
                elif not isinstance(doador, Doador):
                    raise ValueError
                else:
                    return True
        except ValueError:
            self.__tela_doador.mostra_mensagem("Doador não pode ser excluido "
                                               "ou editado por que já fez uma"
                                               " doação, a doação tem que ser "
                                               "excuida primeiro.")
            self.abre_tela_doador()

    def abre_tela_doador(self):
        lista_opcoes = {1: self.cadastrar_doador, 2: self.editar_doador,
                        3: self.remover_doador, 4: self.listar_doador,
                        5: self.buscar_doador, 0: self.retornar}

        while True:
            lista_opcoes[self.__tela_doador.tela_opcoes()]()
