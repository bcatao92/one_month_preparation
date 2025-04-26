matrix = [[112, 42, 83, 119], 
          [56, 125, 56, 49],
          [15, 78, 101, 43], 
          [62, 98, 114, 108]]

def inverteColuna(matriz,coluna):
    aux = []
    n = int(len(matriz))
    for i in range(n):
        aux.append(matriz[i][coluna])
    aux = aux[::-1]
    for j in range(n):
        matriz[j][coluna] = aux[j]    
    return matriz

def inverteLinha(matriz,linha):
    matriz[linha] = matriz[linha][::-1]
    return matriz

def checaLinha(matriz):
    n = int(len(matriz)/2)
    for line in range(n):
        if sum(matriz[line][0:n]) < sum(matriz[line][n:]):
            inverteLinha(matriz,line)
    return(matriz)

def checaColuna(matriz):
    n = len(matriz)
    for linha in range(n):
        for coluna in range(n):


