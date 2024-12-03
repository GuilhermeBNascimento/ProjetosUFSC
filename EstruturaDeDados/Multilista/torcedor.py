class Torcedor:
    def __init__(self, identificador, matricula, nome, curso, cidade_origem, time_torce):
        self.__identificador = identificador
        self.__matricula = matricula
        self.__nome = nome
        self.__curso = curso
        self.__cidade_origem = cidade_origem
        self.__time_torce = time_torce

    def __str__(self):
        return f"ID: {self.__identificador}, Matricula: {self.__matricula}, Nome: {self.__nome}, Curso: {self.__curso}, " \
               f"Cidade de Origem: {self.__cidade_origem}, Time: {self.__time_torce}"
