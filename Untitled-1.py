### Passa a matriz para dicionário
def gridToDic(grid):
    n = len(grid)  # Número de linhas
    m = len(grid[0])  # Número de colunas
    new_grid = {}
    for i in range(n):
        for j in range(m):
            new_grid[i, j] = grid[i][j]
    return new_grid


### Popula o resto da grid com bombas, encontra vizinhos das bombas originais na grid e os explode junto com as bombas originais
def encontraVizinhos(new_grid, guardabombas):
    for k, v in new_grid.items():
        if v == '.':
            new_grid[k] = 'O'
    # Encontra as bombas
    for v in guardabombas.values():
        # Explode bombas e seus vizinhos
        new_grid[v] = '.'
        a, b = v[0], v[1]
        if (a + 1, b) in new_grid:
            new_grid[a + 1, b] = '.'
        if (a - 1, b) in new_grid:
            new_grid[a - 1, b] = '.'
        if (a, b + 1) in new_grid:
            new_grid[a, b + 1] = '.'
        if (a, b - 1) in new_grid:
            new_grid[a, b - 1] = '.'
    return new_grid


def guardaBombas(grid):
    i = 0
    bombas = {}
    for k, v in grid.items():
        if v == "O":
            bombas[i] = k
            i += 1
    return bombas


def bomberMan(n, grid):
    ans = []
    segundos = 0
    m = len(grid)
    k = len(grid[0])
    while segundos < n:
        grid = gridToDic(grid)
        segundos += 1
        bombasOriginais = guardaBombas(grid)
        grid = encontraVizinhos(grid, bombasOriginais)
        segundos += 2
    for i in range(m):
        aux = ''
        for j in range(k):
            aux += grid[i, j]
        ans.append(aux)
    return ans


# Teste
grid = ['.......', '...O...', '....O..', '.......', 'OO.....', 'OO.....']
print(bomberMan(3, grid))