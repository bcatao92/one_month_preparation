k = 4
arr = [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]
arr.sort()
arrb = [arr[0:k+1]]

for i in range(len(arr)-k+1):
    arrb.append(max(arr[i:i+k])-min(arr[i:i+k]))
print(min(arrb))
