from copy import copy


class Bloco(object):
    """
    Classe que contem o Bloco das instrucoes da MT
    """
    (
        RESUME,
        VERBOSE,
        STEP,
        NENHUM
    ) = range(4)

    @property
    def retorne(self):
        return 0

    @property
    def pare(self):
        return 1

    def addListaBlocos(self, blocos):
        self.__listaBlocos = blocos

    def __init__(self, identificador, estado_inicial, instrucoes):
        """
        :param identificador: id do bloco
        :param estado_inicial: estado inicial do bloco
        :param instrucoes: conjunto de instrucoes do bloco no formato {e: {a:tarefa}}
        """
        self.__identificador = identificador
        self.__estadoInicial = estado_inicial
        self.__instrucoes = instrucoes
        self.__listaBlocos = None  # um bloco tera o enderecamento de todos os outros

    def executarBloco(self, fita, dados):
        """
        Executar o bloco no objeto do tipo fita compartilhada por todos os blocos
        :param fita: objeto do tipo fita
        :return: retorne ao bloco anterior ou pare
        """

        # vou para o estado inicial
        estado = self.__estadoInicial

        while True:
            if dados.computacoes == 0:  # usa o prompt para saber se posso continuar
                self.fornecer_opcao(dados)

            if (dados.flag == self.VERBOSE) or (dados.flag == self.STEP):
                formato = "{:->25}: " + fita.printfita
                try:
                    auxstring = ('%s.{:04d}'.format(estado) % self.__identificador)
                except ValueError:
                    auxstring = ('%s.{:0>4s}'.format(estado) % self.__identificador)
                print(formato.format(auxstring))

            # uma computacao realizada
            dados.subcomputacoes(1)

            if estado == 'retorne':
                return self.retorne
            if estado == 'pare':
                print('Resultado: ' + fita.printfita)
                return self.pare

            estado = int(estado)
            instrucoes_estado = self.__instrucoes[estado]

            if type(instrucoes_estado) == list:  # instrucao de movimento para algum bloco
                flag = self.retorne
                dados.chamarbloco(instrucoes_estado[0]).executarBloco(fita, dados)

                if flag == self.pare:
                    return self.pare
                estado = instrucoes_estado[1]
                continue

            caracter = fita.cabecote  # caracter na fita
            break_point = ''
            try:
                break_point = copy(instrucoes_estado[caracter][-1])
                fita.executar(instrucoes_estado[caracter][1:3])
                estado = instrucoes_estado[caracter][3]
                if '!' == break_point:
                    print('breakpoint')
                    self.fornecer_opcao(dados)
            except KeyError:
                try:
                    break_point = copy(instrucoes_estado['∗'][-1])
                    fita.executar(instrucoes_estado['∗'][1:3])
                    estado = instrucoes_estado['∗'][3]
                    if '!' == break_point:
                        print('breakpoint')
                        self.fornecer_opcao(dados)
                except KeyError:
                    try:
                        break_point = copy(instrucoes_estado['*'][-1])
                        fita.executar(instrucoes_estado['*'][1:3])
                        estado = instrucoes_estado['*'][3]
                        if '!' == break_point:
                            print('breakpoint')
                            self.fornecer_opcao(dados)
                    except KeyError:
                        print('Erro no estado %s no bloco %s' %(estado, self.__identificador))
                        print('Caracter %s nao reconhecido' %caracter)
                        exit(-1)

    def fornecer_opcao(self, dados):
        opcao = input('Forneca uma opcao (-r, -v, -s): ')
        opcao = opcao.split()
        if '-r' in opcao[0]:
            dados.alterarflag(self.RESUME)
            dados.addcomputacoes(500)
        if '-v' in opcao[0]:
            print('entrou')
            dados.alterarflag(self.VERBOSE)
            dados.addcomputacoes(500)
        if '-s' in opcao[0]:
            try:
                dados.addcomputacoes(opcao[1])
            except IndexError:
                print('Forneca um inteiro apos o argumento -s')
                self.fornecer_opcao(dados)