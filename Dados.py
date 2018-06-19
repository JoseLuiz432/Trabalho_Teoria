class Dados(object):
    (
        RESUME,
        VERBOSE,
        STEP,
        NENHUM
    ) = range(4)

    def addcomputacoes(self, qnt):
        try:
            self.__computacoes += int(qnt)
        except ValueError:
            print('Valor informado esta incorreto')
    @property
    def computacoes(self):
        return self.__computacoes

    def subcomputacoes(self, qnt):
        try:
            self.__computacoes -= int(qnt)
        except ValueError:
            print('Valor informado esta incorreto')

    def alterarflag(self, flag):
        self.__flag = flag

    @property
    def flag(self):
        return self.__flag

    def chamarbloco(self, nome):
        try:
            return self.__blocos[nome]
        except KeyError:
            print('Erro no estado %s no bloco %s' % (estado, self.__identificador))
            print('Bloco %s nao encontrado' % instrucoes_estado[0])
            exit(-1)

    def __init__(self, numcomputacoes, flag, listaBlocos):
        self.__computacoes = numcomputacoes
        self.__flag = flag
        self.__blocos = listaBlocos