#####
#####           Completar encontraVizinhos

def encontraVizinhos(grid):
    n,m = len(grid), len(grid[0])
    bombas = [['O']*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'O':
                bombas[i][j] = '.'
                if i - 1 >= 0:
                    bombas[i-1][j] = '.'
                if i + 1 <= m:
                    bombas[i+1][j] = '.' 
                if j - 1 >= 0:
                    bombas[i][j-1] = '.'
                if j + 1 <= n:
                    bombas[i][j+1] = '.'
    for i in range(len(bombas)):
        bombas[i] = ''.join(bombas[i])
    return bombas

def bomberMan(n, grid):
    if n == 1: return grid
    
    x,m = len(grid), len(grid[0])
    
    if n % 2 == 0:
        return ['O'*m for _ in range(x)]
    
    explosao = encontraVizinhos(grid)
    explosao2 = encontraVizinhos(explosao)

    if n%4 == 1:
        return explosao2
    if n%4 == 3:
        return explosao

n = 5
grid = ['.......',
'...O.O.',
'....O..',
'..O....',
'OO...OO',
'OO.O...']
