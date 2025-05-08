def encontraVizinhos(grid):
    for a in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[a][j] == "O":
                grid[a][j] = "."
                if grid[a][j + 1] in grid:
                    grid[a][j + 1] = "."
                if grid[a][j - 1] in grid:
                    grid[a][j - 1] = "."
                if grid[a - 1][j] in grid:
                    grid[a - 1][j + 1] = "."
                if grid[a + 1][j] in grid:
                    grid[a + 1][j] = "."
    return grid


def bomberMan(n, grid):
    if n == 1 or (n - 1) % 4 == 0:
        return grid
    gridfull = []
    for i in range(len(grid)):
        aux = []
        for j in range(len(grid[0])):
            aux.append(grid[i][j])
        gridfull.append(aux)
    if n % 2 == 0:
        return gridfull
    if (n + 1) % 4 == 0:
        return encontraVizinhos(grid)


n = 3
grid = ["...", ".O.", "..."]

print(bomberMan(3,grid))