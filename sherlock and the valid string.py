s = 'abc'

def isValid(s):
    a = list(s)
    b = set(a)
    dici=[]
    for letra in b:
        dici.append(a.count(letra))
    dici.sort(reverse=True)
    c = set(dici)
    print(c)
    if(len(c)) == 1: return "YES"
    if len(c) > 2: return "NO"
    if max(c)-min(c) > 1: return "NO"

    for i in range(len(dici)-1):
        if dici[i] != dici[i+1]: 
            if dici[i]-1 == dici[i+1]:
                return "YES"
            else: return "NO"
    return "YES"
print(isValid(s))