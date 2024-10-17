import heapq

# Função para calcular a distância de Manhattan
def manhattan_distance(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

# Função para encontrar o caminho entre dois pinos
def find_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Cima, baixo, esquerda, direita
    visited = set()
    pq = []
    heapq.heappush(pq, (0, start))  # Fila de prioridade (custo, posição)
    parent_map = {start: None}  # Mapear cada célula para o pai, para reconstruir o caminho

    while pq:
        cost, current = heapq.heappop(pq)

        if current == end:
            # Reconstruir o caminho a partir do mapa de pais
            path = []
            while current:
                path.append(current)
                current = parent_map[current]
            return path[::-1]  # Inverter o caminho

        visited.add(current)

        for direction in directions:
            new_row, new_col = current[0] + direction[0], current[1] + direction[1]

            if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited:
                if grid[new_row][new_col] == 0 or (new_row, new_col) == end:  # Espaço vazio ou destino
                    new_cost = cost + 1 + manhattan_distance((new_row, new_col), end)
                    parent_map[(new_row, new_col)] = current
                    heapq.heappush(pq, (new_cost, (new_row, new_col)))

    return None  # Sem caminho encontrado

# Função para marcar o caminho na grade
def mark_path(grid, path, marker):
    for row, col in path:
        grid[row][col] = marker

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

# Coordenadas dos pinos
start_red_1 = (3, 3)
start_red_2 = (18, 8)

start_green_1 = (9, 19)
start_green_2 = (13, 3)

start_blue_1 = (4, 17)
start_blue_2 = (17, 2)

# Conectar pinos vermelhos
path_red = find_path(grid, start_red_1, start_red_2)
if path_red:
    print("Caminho encontrado para pinos vermelhos:", path_red)
    mark_path(grid, path_red, 2)  # Marcar caminho com 5
else:
    print("Nenhum caminho encontrado para pinos vermelhos.")

# Conectar pinos verdes
path_green = find_path(grid, start_green_1, start_green_2)
if path_green:
    print("Caminho encontrado para pinos verdes:", path_green)
    mark_path(grid, path_green, 3)  # Marcar caminho com 6
else:
    print("Nenhum caminho encontrado para pinos verdes.")

# Conectar pinos azuis
path_blue = find_path(grid, start_blue_1, start_blue_2)
if path_blue:
    print("Caminho encontrado para pinos azuis:", path_blue)
    mark_path(grid, path_blue, 4)  # Marcar caminho com 7
else:
    print("Nenhum caminho encontrado para pinos azuis.")

# Exibir a matriz resultante
for row in grid:
    print(row)
