import heapq
import matplotlib.pyplot as plt
import numpy as np

def manhattan_distance(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

def find_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()
    pq = []
    heapq.heappush(pq, (0, 0, start))
    parent_map = {start: None}

    while pq:
        cost, path_length, current = heapq.heappop(pq)

        if current == end:
            path = []
            while current:
                path.append(current)
                current = parent_map[current]
            return path[::-1], path_length

        visited.add(current)

        for direction in directions:
            new_row, new_col = current[0] + direction[0], current[1] + direction[1]

            if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited:
                if grid[new_row][new_col] == 0 or (new_row, new_col) == end:
                    new_cost = path_length + 1 + manhattan_distance((new_row, new_col), end)
                    parent_map[(new_row, new_col)] = current
                    heapq.heappush(pq, (new_cost, path_length + 1, (new_row, new_col)))

    return None, 0

def mark_path(grid, path, marker):
    for row, col in path:
        grid[row][col] = marker

def connect_pins(grid, pairs):
    connected_pairs = 0
    total_path_length = 0

    for pair, marker in pairs:
        start, end = pair
        path, path_length = find_path(grid, start, end)
        if path:
            connected_pairs += 1
            total_path_length += path_length
            mark_path(grid, path, marker)
        else:
            print(f"Nenhum caminho encontrado para pinos em {start} e {end}.")

    return connected_pairs, total_path_length

def plot_grid(grid):
    grid_np = np.array(grid)
    cmap = plt.cm.colors.ListedColormap(['white', 'black', 'red', 'green', 'blue'])
    bounds = [0, 1, 2, 3, 4, 5]
    norm = plt.cm.colors.BoundaryNorm(bounds, cmap.N)

    plt.figure(figsize=(10, 10))  # Ajuste o tamanho da figura
    plt.imshow(grid_np, cmap=cmap, norm=norm)
    plt.grid(False)
    plt.title("Matriz com Caminhos Conectados")

    # Adicionando anotações para os pinos
    for i, (pair, marker) in enumerate(pairs):
        start, end = pair
        plt.annotate('P1', (start[1], start[0]), color='black', fontsize=12, ha='center')
        plt.annotate('P2', (end[1], end[0]), color='black', fontsize=12, ha='center')

    plt.savefig('matriz_caminhos.png')  # Salva a imagem
    plt.show()

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
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Definir pares de pinos a serem conectados e seus marcadores
pairs = [(((1, 1), (14, 3)), 2), (((1, 1), (14, 4)), 3)]

# Conectar os pinos e obter estatísticas
connected_pairs, total_path_length = connect_pins(grid, pairs)

print(f"Número de pares conectados: {connected_pairs}")
print(f"Comprimento total dos caminhos: {total_path_length}")

# Gerar a imagem da matriz
plot_grid(grid)
