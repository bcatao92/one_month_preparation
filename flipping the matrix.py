matrix = [[112, 42, 83, 119], 
          [56, 125, 56, 49],
          [15, 78, 101, 43], 
          [62, 98, 114, 108]]
n = len(matrix)
m = int(n/2)

for i in range(m):
    pm,sm=0,0                   #primeira metade, segunda metade
    for j in range(m):
        pm+=matrix[j][i]
        sm+=matrix[j+m][i]
    for j in range(n):    
            matrix[j][i], matrix[n - 1 - j][i] = matrix[n - 1 - j][i], matrix[j][i]


print(matrix)
