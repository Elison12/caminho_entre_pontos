import random

def gerar_mapa(largura, altura):
    """Gera um mapa aleatório com as especificações dadas.

    Args:
        largura: Largura do mapa.
        altura: Altura do mapa.

    Returns:
        Uma lista de listas representando o mapa.
    """

    mapa = [[0 for _ in range(largura)] for _ in range(altura)]

    # Garantindo pelo menos um par de cada cor
    cores = [2, 3, 4]
    for cor in cores:
        while True:
            x1 = random.randint(0, largura - 1)
            y1 = random.randint(0, altura - 1)
            x2 = random.randint(0, largura - 1)
            y2 = random.randint(0, altura - 1)

            if mapa[y1][x1] == 0 and mapa[y2][x2] == 0:
                mapa[y1][x1] = cor
                mapa[y2][x2] = cor
                break

    # Preenchendo o restante do mapa aleatoriamente
    for y in range(altura):
        for x in range(largura):
            if mapa[y][x] == 0:
                mapa[y][x] = random.choice([0, 1])  # Espaço ou barreira

    return mapa

# Exemplo de uso:
mapa = gerar_mapa(20, 15)

# Imprimindo o mapa
for linha in mapa:
    print(linha)