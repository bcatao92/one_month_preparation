def encontraVizinhos(grid[a][b]):
    
    return -1


def bomberMan(n,grid):
    if n == 1 or (n-1)%4==0: return grid
    gridfull = []
    for i in range(len(grid)):
        aux = []
        for j in range(len(grid)):
            aux.append(grid[i][j])
        gridfull.append(aux)
    if n%2 == 0: return gridfull
