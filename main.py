import sys

import numpy as np
from contabilize import connect_pins, find_specific_pairs
from escrever_arquivo import write_results_to_file
import generate_image
from ler_arquivo import ler_matriz_de_arquivo


if __name__ == '__main__':

    caminho_arquivo = sys.argv[1]

    grid = ler_matriz_de_arquivo(caminho_arquivo)

    target = [2, 3, 4]
    posicoes = find_specific_pairs(grid=grid, targets=target)
    
        
    pRed = posicoes.get(2)[0]
    qRed = posicoes.get(2)[1]

    pGreen = posicoes.get(3)[0]
    qGreen = posicoes.get(3)[1]

    pBlue = posicoes.get(4)[0]
    qBlue = posicoes.get(4)[1]

    pairs = [
        ((pRed, qRed), 2),
        ((pGreen, qGreen), 3),
        ((pBlue, qBlue), 4)
    ]
    
    connected_pairs, total_path_length = connect_pins(grid, pairs)
    
    write_results_to_file('resultado_X.txt', connected_pairs, total_path_length, grid)
    
    matrix = np.array(grid)

    # gera a imagem
    image = generate_image.generate_image(matrix)

    # salva a imagem
    image.save("solucao_X.png")
    # image.show()  # para mostrar a imagem