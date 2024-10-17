import heapq
import numpy as np
from PIL import Image


# Função para gerar a imagem a partir da matriz
def generate_image(matrix):
    # Define as cores
    colors = {
        0: (255, 255, 255),  # Branco
        1: (0, 0, 0),        # Preto
        2: (255, 0, 0),      # Vermelho
        3: (0, 255, 0),      # Verde
        4: (0, 0, 255)       # Azul
    }

    # Cria uma imagem RGB a partir da matriz
    height, width = matrix.shape
    image = Image.new("RGB", (width, height))

    # Preenche a imagem com as cores da matriz
    for y in range(height):
        for x in range(width):
            image.putpixel((x, y), colors[matrix[y, x]])

    return image


# Função para calcular a distância de Manhattan
def manhattan_distance(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

# Função para encontrar o caminho entre dois pinos
def find_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Cima, baixo, esquerda, direita
    visited = set()
    pq = []
    heapq.heappush(pq, (0, 0, start))  # Fila de prioridade (custo, comprimento, posição)
    parent_map = {start: None}  # Mapear cada célula para o pai, para reconstruir o caminho

    while pq:
        cost, path_length, current = heapq.heappop(pq)

        if current == end:
            # Reconstruir o caminho a partir do mapa de pais
            path = []
            while current:
                path.append(current)
                current = parent_map[current]
            return path[::-1], path_length  # Retornar caminho e comprimento

        visited.add(current)

        for direction in directions:
            new_row, new_col = current[0] + direction[0], current[1] + direction[1]

            if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited:
                if grid[new_row][new_col] == 0 or (new_row, new_col) == end:  # Espaço vazio ou destino
                    new_cost = path_length + 1 + manhattan_distance((new_row, new_col), end)
                    parent_map[(new_row, new_col)] = current
                    heapq.heappush(pq, (new_cost, path_length + 1, (new_row, new_col)))

    return None, 0  # Sem caminho encontrado

# Função para marcar o caminho na grade
def mark_path(grid, path, marker):
    for row, col in path:
        grid[row][col] = marker

# Função para conectar pinos e calcular estatísticas
def connect_pins(grid, pairs):
    connected_pairs = 0
    total_path_length = 0

    for pair, marker in pairs:
        start, end = pair
        path, path_length = find_path(grid, start, end)
        if path:
            connected_pairs += 1
            total_path_length += path_length
            mark_path(grid, path, marker)  # Marcar o caminho na grid
        else:
            print(f"Nenhum caminho encontrado para pinos em {start} e {end}.")

    return connected_pairs, total_path_length

# Definição da grid
grid = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 3, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Coordenadas dos pinos
start_red = (3, 3)
end_red = (18, 8)

start_green = (9, 18)
end_green = (13, 3)

start_blue = (4, 17)
end_blue = (17, 2)

# Lista de pares para conectar (start, end) e seus marcadores
pairs = [
    ((start_red, end_red), 2),   # Vermelho
    ((start_green, end_green), 3),  # Verde
    ((start_blue, end_blue), 4)    # Azul
]

# Conectar os pinos e obter estatísticas
connected_pairs, total_path_length = connect_pins(grid, pairs)

print(f"Número de pares conectados: {connected_pairs}")
print(f"Comprimento total dos caminhos: {total_path_length}")

# Exibir a grid com os caminhos marcados
for row in grid:
    print(row)

# Converte a lista de listas em um array numpy
matrix = np.array(grid)

# Gera a imagem
image = generate_image(matrix)

# Salva a imagem
image.save("output_image.png")
image.show()  # Para mostrar a imagem
