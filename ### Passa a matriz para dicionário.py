### Passa a matriz para dicionário
def gridToDic(grid):
    n = len(grid)
    m = len(grid[0])
    new_grid = {}
    for i in range(n):
        for j in range(m):
            new_grid[i, j] = grid[i][j]
    return new_grid


### Explode bombas e seus vizinhos
def encontraVizinhos(new_grid, guardabombas):
    for k, v in new_grid.items():
        if v == ".":
            new_grid[k] = "O"
    # Explode bombas e seus vizinhos
    for v in guardabombas:
        new_grid[v] = "."
        a, b = v
        if (a + 1, b) in new_grid:
            new_grid[a + 1, b] = "."
        if (a - 1, b) in new_grid:
            new_grid[a - 1, b] = "."
        if (a, b + 1) in new_grid:
            new_grid[a, b + 1] = "."
        if (a, b - 1) in new_grid:
            new_grid[a, b - 1] = "."
    return new_grid


### Identifica as bombas na grade
def guardaBombas(grid):
    bombas = []
    for k, v in grid.items():
        if v == "O":
            bombas.append(k)
    return bombas


def bomberMan(n, grid):
    if n == 1:
        return grid  # Caso especial: nenhuma bomba explode no primeiro segundo

    if n % 2 == 0:
        # Caso especial: em segundos pares, toda a grade está cheia de bombas
        return ["O" * len(grid[0]) for _ in range(len(grid))]

    # Converte a grade para um dicionário
    grid_dict = gridToDic(grid)

    # Simula o comportamento para ciclos de 4 segundos
    for _ in range((n - 1) % 4 + 1):
        bombasOriginais = guardaBombas(grid_dict)
        grid_dict = encontraVizinhos(grid_dict, bombasOriginais)

    # Converte o dicionário de volta para a grade
    ans = []
    for i in range(len(grid)):
        aux = ""
        for j in range(len(grid[0])):
            aux += grid_dict[i, j]
        ans.append(aux)

    return ans


# Teste
grid = [
    ".......",
    "...O.O.",
    "....O..",
    "..O....",
    "OO...OO",
    "OO.O...",
]

print(bomberMan(5, grid))

expected_output = [
    ".......",
    "...O.O.",
    "...OO..",
    "..OOOO.",
    "OOOOOOO",
    "OOOOOOO",
]