import heapq
import numpy as np


def find_specific_pairs(grid, targets):
    """
    retorna as posições dos pinos
    """
    paired_positions = {target: [] for target in targets}
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            value = grid[i][j]
            if value in targets:
                paired_positions[value].append((i, j))
    
 
    paired_positions = {key: positions for key, positions in paired_positions.items() if positions}
    
    return paired_positions

def manhattan_distance(start, end):
    """
    Função para calcular a distância de Manhattan
    """
    return abs(start[0] - end[0]) + abs(start[1] - end[1])
def find_path(grid, start, end):
    """
    Função para encontrar o caminho entre dois pinos
    """
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Cima, baixo, esquerda, direita
    visited = set()
    pq = []
    heapq.heappush(pq, (0, 0, start))  # Fila de prioridade (custo, comprimento, posição)
    parent_map = {start: None}  # Mapear cada célula para o pai, para reconstruir o caminho

    if start == end:  # Adicione esta verificação
        return [start], 0

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
                    visited.add((new_row, new_col))  # Certifique-se de adicionar à lista de visitados

    return None, 0  # Sem caminho encontrado

def mark_path(grid, path, marker):
    """
    Função para marcar o caminho na grade
    """
    for row, col in path:
        grid[row][col] = marker

def connect_pins(grid, pairs):

    """
    Função para conectar pinos e calcular estatísticas
    """
    connected_pairs = 0
    total_path_length = 0

    for pair, marker in pairs:
        start, end = pair
        path, path_length = find_path(grid, start, end)
        if path:
            connected_pairs += 1
            total_path_length += path_length
            mark_path(grid, path, marker)
        # else:
            # print(f"nenhum caminho encontrado para pinos em {start} e {end}.")

    return connected_pairs, total_path_length
