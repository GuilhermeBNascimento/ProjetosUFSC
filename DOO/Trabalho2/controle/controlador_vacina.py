from entidade.gato import Gato
from entidade.cachorro import Cachorro
from limite.tela_vacina import TelaVacina
from entidade.vacina import Vacina


class ControladorVacina:
    def __init__(self, controlador_sistema):
        self.__tela_vacina = TelaVacina()
        self.__controlador_sistema = controlador_sistema

    def cadastrar_vacina(self, animal):
        dados_vacina = self.__tela_vacina.pega_dados_vacina()
        if dados_vacina["opcao"] == 'Confirmar':
            nome_vacina = (dados_vacina["nome_vacina"])
            try:
                vacina = self.pega_vacina_por_nome(nome_vacina, animal)
                if vacina is not None:
                    raise ValueError
                else:
                    data_vacina = (dados_vacina["data_vacina"])
                    vacina = Vacina(nome_vacina, data_vacina)
                    animal.vacinas.append(vacina)

            except ValueError:
                self.__tela_vacina.mostra_mensagem("ERRO: Animal já recebeu "
                                                   "essa vacina!")

    def editar_vacina(self, animal):
        try:
            if animal.vacinas is not None:
                self.listar_vacinas(animal)
                vacina_selecionada = self.__tela_vacina.seleciona_vacina()
                for vacina in animal.vacinas:
                    if vacina.nome_vacina == vacina_selecionada:
                        animal.vacinas.remove(vacina)
                        dados_vacina = self.__tela_vacina.pega_dados_vacina({"nome_vacina": vacina.nome_vacina, "ano": vacina.ano, "mes": vacina.mes,
                                                                             "dia": vacina.dia, "data_vacina": vacina.data_vacina})
                        nome_vacina = (dados_vacina["nome_vacina"])
                        data_vacina = (dados_vacina["data_vacina"])
                        vacina = Vacina(nome_vacina, data_vacina)
                        animal.vacinas.append(vacina)
                    else:
                        raise ValueError
            else:
                raise ValueError

        except ValueError:
            self.__tela_vacina.mostra_mensagem("ERRO: Animal não possui"
                                               " essa vacina")

    def remover_vacina(self, animal):
        try:
            if animal.vacinas is not None:
                self.listar_vacinas(animal)
                vacina_selecionada = self.__tela_vacina.seleciona_vacina()
                for vacina in animal.vacinas:
                    if vacina.nome_vacina == vacina_selecionada:
                        animal.vacinas.remove(vacina)
                    else:
                        raise ValueError
            else:
                raise ValueError
        except ValueError:
            self.__tela_vacina.mostra_mensagem("Erro, vacina não "
                                               "pode ser excluida")

    def listar_vacinas(self, animal):
        try:
            if animal.vacinas is not None:
                    self.__tela_vacina.mostra_vacina(animal.vacinas)
            else:
                raise ValueError
        except ValueError:
            self.__tela_vacina.mostra_mensagem("Animal não possui "
                                               "vacinas cadastradas")

    def pega_vacina_por_nome(self, nome_vacina, animal):
        for vacina in animal.vacinas:
            if vacina.nome_vacina == nome_vacina:
                return vacina
            else:
                return None

    def retornar(self, animal):
        tipo_animal = animal.numero_chip
        tipo_animal = tipo_animal[0]
        if tipo_animal == "G":
            self.__controlador_sistema.controlador_gatos.abre_tela_gato()
        elif tipo_animal == "C":
            self.__controlador_sistema.controlador_cachorros.\
                abre_tela_cachorro()
        else:
            self.__controlador_sistema.abre_tela()

    def abre_tela_vacina(self, animal):
        try:
            if isinstance(animal, Gato) or isinstance(animal, Cachorro):
                while True:
                    lista_opcoes = self.__tela_vacina.tela_opcoes()
                    if lista_opcoes == 1:
                        self.cadastrar_vacina(animal)
                    elif lista_opcoes == 2:
                        self.editar_vacina(animal)
                    elif lista_opcoes == 3:
                        self.remover_vacina(animal)
                    elif lista_opcoes == 4:
                        self.listar_vacinas(animal)
                    elif lista_opcoes == 0:
                        self.retornar(animal)
                    else:
                        raise ValueError
            else:
                raise ValueError
        except ValueError:
            print("Erro no tipo de informação passada para o "
                  "controle das Vacinas")
            self.__controlador_sistema.abre_tela()