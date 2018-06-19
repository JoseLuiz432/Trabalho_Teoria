
class InputFile(object):
    def leitura_arquivo(self, nome_arquivo):
        """
        leitura do arquivo
        :param nome_arquivo: nome do arquivo *.MT
        :return:
        """
        arquivo = ''

        try:
            arquivo = open(nome_arquivo, 'r')
        except:
            print("Arquivo %s nao encontrado" %nome_arquivo)
            exit()

        leitura = arquivo.readlines()

        arquivo.close()

        return leitura


