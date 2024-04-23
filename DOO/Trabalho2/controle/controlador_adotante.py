from entidade.adotante import Adotante
from limite.tela_adotante import TelaAdotante
from persistencia.adotante_dao import AdotanteDAO


class ControladorAdotante:
    def __init__(self, controlador_sistema):
        self.__adotante_dao = AdotanteDAO()
        self.__tela_adotante = TelaAdotante()
        self.__controlador_sistema = controlador_sistema

    @property
    def adotantes(self):
        return self.__adotante_dao.pega_todos()

    def pega_adotante_por_cpf(self, cpf: int):
        for adotante in self.__adotante_dao.pega_todos():
            if adotante.cpf == cpf:
                return adotante
            else:
                return None

    def cadastrar_adotante(self):
        dados_adotante = self.__tela_adotante.pega_dados_adotante()
        if dados_adotante["opcao"] == 'Confirmar':
            adotante = self.pega_adotante_por_cpf(dados_adotante["cpf"])

            try:
                if adotante is None:
                    adotante = Adotante(dados_adotante["nome"], dados_adotante["cpf"],
                                        dados_adotante["data_nascimento"], dados_adotante["endereco"],
                                        dados_adotante["tipo_habitacao"], dados_adotante["tamanho_residencia"],
                                        dados_adotante["possui_animal"])
                    self.__adotante_dao.adiciona(adotante)
                    self.__tela_adotante.mostra_mensagem("Adotante adicionado"
                                                         " com sucesso.")
                else:
                    raise ValueError
            except ValueError:
                self.__tela_adotante.mostra_mensagem("ERRO: Adotante já existe!.")

    def editar_adotante(self):
        self.listar_adotante()
        cpf_adotante = self.__tela_adotante.seleciona_adotante()
        if cpf_adotante is not None:
            adotante = self.pega_adotante_por_cpf(cpf_adotante)

            try:
                if adotante is not None:
                    self.checa_adotante(adotante)
                    novos_dados_adotante = \
                        self.__tela_adotante.pega_dados_adotante({"nome": adotante.nome, "cpf": adotante.cpf, "ano": adotante.data_nascimento.year,
                                                                  "mes": adotante.data_nascimento.month, "dia": adotante.data_nascimento.day, "endereco": adotante.endereco,
                                                                  "tipo_habitacao": adotante.tipo_habitacao, "tamanho_residencia": adotante.tamanho_residencia,
                                                                  "possui_animal": adotante.possui_animal})
                    adotante.nome = novos_dados_adotante["nome"]
                    adotante.cpf = novos_dados_adotante["cpf"]
                    adotante.data_nascimento = \
                        novos_dados_adotante["data_nascimento"]
                    adotante.endereco = novos_dados_adotante["endereco"]
                    adotante.tipo_habitacao = \
                        novos_dados_adotante["tipo_habitacao"]
                    adotante.tamanho_residencia = \
                        novos_dados_adotante["tamanho_residencia"]
                    adotante.possui_animal = novos_dados_adotante["possui_animal"]
                    self.__tela_adotante.mostra_mensagem("Adotante alterado"
                                                         " com sucesso.")
                    self.listar_adotante()
                else:
                    raise ValueError
            except ValueError:
                self.__tela_adotante.mostra_mensagem("ERRO: Adotante não existe!.")

    def listar_adotante(self):
        adotantes = []
        for adotante in self.__adotante_dao.pega_todos():
            adotantes.append({"nome": adotante.nome,
                                                  "cpf": adotante.cpf,
                                                  "data_nascimento":
                                                  adotante.data_nascimento,
                                                  "endereco": adotante.
                                                  endereco,
                                                  "tipo_habitacao": adotante.
                                                  tipo_habitacao,
                                                  "tamanho_residencia":
                                                  adotante.tamanho_residencia,
                                                  "possui_animal":
                                                  adotante.possui_animal})
        self.__tela_adotante.mostra_adotante(adotantes)

    def remover_adotante(self):
        self.listar_adotante()
        self.__tela_adotante.mostra_mensagem("CPF do Adotante que "
                                             "queira remover:")
        cpf_adotante = self.__tela_adotante.seleciona_adotante()
        adotante = self.pega_adotante_por_cpf(cpf_adotante)

        try:
            if adotante is not None:
                self.checa_adotante(adotante)
                self.__adotante_dao.remove(cpf_adotante)
                self.__tela_adotante.mostra_mensagem("Adotante removido "
                                                     "com sucesso.")
                self.listar_adotante()
            else:
                raise ValueError
        except ValueError:
            self.__tela_adotante.mostra_mensagem("ERRO: Adotante não existe!.")

    def pedir_mostra_adotante(self, adotante: Adotante):
        try:
            if adotante is not None:
                self.__tela_adotante.mostra_adotante({"nome": adotante.nome,
                                                      "cpf": adotante.cpf,
                                                      "data_nascimento":
                                                      adotante.data_nascimento,
                                                      "endereco":
                                                      adotante.endereco,
                                                      "tipo_habitacao":
                                                      adotante.tipo_habitacao,
                                                      "tamanho_residencia":
                                                      adotante.
                                                     tamanho_residencia,
                                                     "possui_animal":
                                                      adotante.possui_animal})
            else:
                raise ValueError
        except ValueError:
            self.__tela_adotante.mostra_mensagem("ERRO: Adotante "
                                                 "não foi repassado")

    def checa_adotante(self, adotante):
        try:
            for adocao in self.__controlador_sistema.controlador_adocoes.\
                    registros_adocao:
                if adocao.adotante == adotante:
                    raise ValueError
                else:
                    return adotante
        except ValueError:
            self.__tela_adotante.mostra_mensagem("Adotante não pode ser "
                                                 "excluido ou editado por que"
                                                 " já adotou, a adocao tem que"
                                                 " ser excluida primeiro.")
            self.abre_tela_adotante()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela_adotante(self):
        lista_opcoes = {1: self.cadastrar_adotante, 2: self.editar_adotante,
                        3: self.remover_adotante, 4: self.listar_adotante,
                        0: self.retornar}

        while True:
            lista_opcoes[self.__tela_adotante.tela_opcoes()]()