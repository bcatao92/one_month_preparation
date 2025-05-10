q = [1,2,3,4,5,6,7,8]

q2 = [1,2,3,5,4,6,7,8]

bribes = 0
#for i in range(len(q2)):
#    if q2[i] != i+1:
#        print(q2[i],q[i+1])
#        
#print(bribes)

total1,total2 = 0,0
soma = sum(q)
suborno=0
for i in range(len(q)):
    total1+=q[i]
    total2+=q2[i]
    if total1!=total2:
        suborno+=1
        
    print(total1," ",total2)
print(suborno)