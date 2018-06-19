from Bloco import Bloco


class ConstrutorBlocos(object):
    """
    Classse que constroi os blocos a partir das linhas extraidas do arquivo
    """
    def construir(self, linhas):
        """

        :param linhas: linhas extraidas do arquivo.MT
        :return: {id: Bloco,...} id e bloco equivalente
        """

        # Flag que ira indicar a entrada e saida de um bloco
        flag = False
        id_bloco = ''
        est_inicial = ''
        instrucoes = {}
        blocos = {}
        for linha in linhas:
            linha = linha.split()

            # Se a linha estiver em branco
            if not linha:
                continue


            # comentario
            if ';' in linha[0]:
                continue

            if 'bloco' in linha[0]:
                id_bloco = linha[1]
                est_inicial = int(linha[2])
                instrucoes = {}
                flag = True
                continue

            if 'fim' in linha[0]:
                flag = False
                blocos.update({id_bloco: Bloco(id_bloco, est_inicial, instrucoes)})
                continue

            if flag:
                estado = int(linha[0])
                if estado not in instrucoes.keys():
                    if len(linha[1]) > 1:
                        instrucao = linha[1:]
                    else:
                        instrucao = {linha[1]: linha[2:]}   # { caracter na fita : instrucoes }

                    instrucoes.update({estado: instrucao})
                else:
                    instrucao = {linha[1]: linha[2:]}   # { caracter na fita : instrucoes }
                    instrucoes[estado].update(instrucao)

        return blocos