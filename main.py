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

# Exemplo de matriz 10x10
grid = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1,  0, 0, 0, 0, 0, 0, 2, 0, 1],
    [1,  0, 4, 0, 0, 0, 0, 0, 0, 1],
    [1,  0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1,  0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1,  0, 0, 0, 2, 0, 0, 0, 0, 1],
    [1,  0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1,  0, 0, 0, 0, 0, 0, 4, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Encontrar caminho para pinos vermelhos (2, 2)
start_red = (1, 7)
end_red = (6, 4)

start_blue = (2,3)
end_blue = (8,7)
path_blue = find_path(grid, start_blue, end_blue)

if path_blue:
    print("Caminho encontrado para azul:", path_blue)
else:
    print("Nenhum caminho encontrado para azul.")
