def write_results_to_file(filename, connected_pairs, total_path_length, result_matrix):
    """
    escreve os resultados obtidos em um arquivo
    """
    
    with open(filename, 'w') as file:

        file.write(f"{connected_pairs}\n")
        file.write(f"{total_path_length}\n")
        
        for row in result_matrix:
            file.write(' '.join(map(str, row)) + '\n')