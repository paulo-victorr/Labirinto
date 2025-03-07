from collections import deque

def carregar_labirinto(nome_arquivo):
    """Carrega o labirinto a partir de um arquivo txt."""
    with open(nome_arquivo, 'r') as f:
        return [linha.strip() for linha in f.readlines()]


LABIRINTO = carregar_labirinto("labirinto1.txt")


DIRECOES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def encontrar_inicio(labirinto):
    """ Encontra a posição inicial (S) do jogador. """
    for i, linha in enumerate(labirinto):
        for j, celula in enumerate(linha):
            if celula == 'S':
                return i, j
    return None

def labirinto_backtracking(labirinto):
    """ Resolve o labirinto usando backtracking com pilha. """
    inicio = encontrar_inicio(labirinto)
    if not inicio:
        return False
    
    pilha = deque()
    pilha.append(inicio)
    visitados = set()
    
    while pilha:
        x, y = pilha.pop()
        
        if labirinto[x][y] == 'E':
            return True
        
        visitados.add((x, y))
        
       
        for dx, dy in DIRECOES:
            nx, ny = x + dx, y + dy
            
           
            if 0 <= nx < len(labirinto) and 0 <= ny < len(labirinto[0]) and labirinto[nx][ny] in ('1', 'E') and (nx, ny) not in visitados:
                pilha.append((nx, ny))
    
    return False  


resultado = labirinto_backtracking(LABIRINTO)
print("Caminho encontrado?", resultado)
