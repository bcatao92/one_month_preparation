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

def checaColuna(matriz,coluna):
    n = len(matriz)
    pm,sm = 0,0
    for i in range(int(n/2)):
        #print(matriz[i][coluna])
        pm += matriz[i][coluna]
        sm += matriz[i+int(n/2)][coluna]
    if sm > pm:
        inverteColuna(matriz,coluna)
        return matriz
    return matriz

def somaQuadrante(matriz):
    sum = 0
    n = int(len(matriz)/2)
    for i in range(n):
        for j in range(n):
            sum+=matriz[j][i]
    return sum


def main(matriz):
    n = len(matriz)
    for coluna in range(n):
        checaColuna(matriz,coluna)
    for linha in range(n):
        checaLinha(matriz)
    return(somaQuadrante(matriz))
print(main(matrix))

