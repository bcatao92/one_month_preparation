#q = [5,1,2,3,4,6,8,7]
#q = [4,1,2,3]
#q = [2,1,5,3,4]
#q = [5,1,2,3,7,8,6,4]
q = [1,2,5,3,7,8,6,4]
def minimumBribes(q):
    for i in range(len(q)):
        if (q[i]-(i+1))>2:
            print("Too chaotic")
            return
    swap=0
    for i in range(len(q)):
        s=0
        for j in range(0,len(q)-i-1):
            if q[j]>q[j+1]:
                q[j],q[j+1]=q[j+1],q[j]
                s+=1
        if s==0:
            break
        swap+=s

    print(swap)
    return

minimumBribes(q)