matrix = [[112, 42, 83, 119], 
          [56, 125, 56, 49],
          [15, 78, 101, 43], 
          [62, 98, 114, 108]]
n2 = len(matrix)
n = n2/2

def inverteLinha(matriz,linha):
    aux = []
    for i in range(1,len(matriz[linha])):
        aux.append(matrix[linha][-i])
    aux.append(matrix[linha][0])
    for i in range(len(aux)):
        matriz[linha][i] = aux[i]
    return matrix

def inverteColuna(matriz,coluna):
    aux = []
    for i in range(1,len(matriz)):
        aux.append(matriz[-i][coluna])
    aux.append(matriz[0][coluna])
    for i in range(len(aux)):
        matriz[i][coluna] = aux[i]
    return matriz

