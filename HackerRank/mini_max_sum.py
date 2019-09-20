
arr = list(map(int, input().rstrip().split()))

arr.sort()
min = 0
max = 0
for i in range(4):
    max += arr[(i+1)*-1]
    min += arr[i]

print(min, max)