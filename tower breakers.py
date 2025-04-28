#Lógica: criar um array contendo as torres
#Cada jogada vai pegar a maior torre disponível e 
# reduzi-la por um divisor exato de sua altura
#Cada iteração acrescenta 1 ao res
#Se res for par, ganha o jogador 2, senão, o 1


def maiorDivisor(m):
    if m%2 == 0:
        return int(m/2)
    a = m//2
    while m%a!=0:
        a-=1
    return a

def selecionaTorre(torres):
    res = 0
    while max(torres)!= 1:
        alvo = torres.index(max(torres))
        torres[alvo] = torres[alvo]/maiorDivisor(torres[alvo])
        res+=1
    return res


def towerBreakers(n,m):
    aux = []
    for i in range(1,n+1): #preenche o array com as torres
        aux.append(m)
    res = selecionaTorre(aux)   
    if res%2 == 0: return 2 
    return 1

print(towerBreakers(2,2))
