import re


def ler_matriz_de_arquivo(caminho_arquivo):
    '''
    método para ler o arquivo txt passado por argumento
    '''
    with open(caminho_arquivo, 'r') as arquivo:
        grid = []
        for linha in arquivo:
            linha_formatada = list(map(int, re.findall(r'\d', linha)))
            grid.append(linha_formatada)
    return grid
