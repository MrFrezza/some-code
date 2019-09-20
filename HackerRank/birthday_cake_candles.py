arr = list(map(int, input().rstrip().split()))

arr.sort(reverse=True)
qtd = 0
ctr = 0
tam = len(arr)
while arr[ctr] == arr[0]:
    qtd +=1
    ctr +=1
    if ctr == tam:
        break

print(arr)
print(qtd)