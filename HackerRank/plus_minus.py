n = int(input())

arr = list(map(int, input().rstrip().split()))

qtdNeg = 0
qtdZer = 0
qtdPos = 0

for i in arr:
    if i > 0:
        qtdPos += 1
    elif i < 0:
        qtdNeg += 1
    elif i == 0:
        qtdZer += 1
    
print(qtdPos/n)
print(qtdNeg/n)
print(qtdZer/n)