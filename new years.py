#q = [1,2,3,5,4,6,7,8]
q = [4,1,2,3]
n = len(q)

suborno = 0

i = 0
while i < n:
#for i in range(n):
    if q[i] != i+1:
        print(q[i])
        a = q[i]-q[i+1]
        i+=1
        if a == 1:
            suborno+=1
        elif a == 2:
            suborno+=2
        else:
            print("Too chaotic")
            quit()
    i+=1
print("Subornos: ",suborno)