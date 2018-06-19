
import argparse
from InputFile import InputFile
from ConstrutorBlocos import ConstrutorBlocos
from Fita import Fita
from Dados import Dados


class Main(object):

    @staticmethod
    def Main():
        # flags constantes para auxiliar
        (
            RESUME,
            VERBOSE,
            STEP,
            NENHUM
        ) = range(4)

        # instanciando os objetos  basicos
        parser = argparse.ArgumentParser()
        entrada = InputFile()
        # adicionando os argumentos de entrada do arquivo
        parser.add_argument(
            '-r',
            '--resume',
            action='store_true',
            help='Executa o programa ate o fim em modo silencioso e depois imprime o conteudo no final da fita.'

        )
        parser.add_argument(
            '-v',
            '--verbose',
            action='store_true',
            help='Mostra a execucao passo a passo do programa ate o fim.'
        )

        parser.add_argument(
            '-s',
            '--step',
            type=int,
            help="""mostra n computacoes passo a passo na tela, depois abre prompt e
aguarda nova opcao (-r,-v,-s). Caso nao seja fornecida nova opcao (entrada em branco), o padrao
e repetir a ultima opcao."""
        )
        parser.add_argument(
            '--head',
            type=str,
            help='Modifica os delimitadores do cabecote que sao por padrao ( e ).'
        )
        parser.add_argument(
            'nome_arquivo',
            type=str,
            help='Nome do arquivo *.MT.',
        )
        args = parser.parse_args()
        linhas = entrada.leitura_arquivo(args.nome_arquivo)
        construtor = ConstrutorBlocos()
        blocos = construtor.construir(linhas)
        flag = NENHUM
        caracter_cabecote = '()'

        # verificacao das opcoes utilizadas
        if args.step:
            flag = STEP
            computacoes = args.step
        else:
            computacoes = 500 # numero padrao de computacoes
        if args.resume:
            flag = RESUME

        if args.head:
            caracter_cabecote = args.head

        if args.verbose:
            flag = VERBOSE


        # boas vindas
        boasvindas = """
        Simulador de Maquina de Turing ve r 1. 0
        Desenvolvido como trabalho pratico para a diciplina Teoria da Computacao
        Jose Luiz Maciel Pimenta, IFMG, 2018
        """
        print(boasvindas)
        # entrada da palavra fornecida pelo prompt
        palavra = input('Forneca a palavra inicial: ')
        fita = Fita(palavra, caracter_cabecote)
        dados = Dados(computacoes, flag, blocos)
        # executar o bloco main
        blocos['main'].executarBloco(fita, dados)


Main.Main()