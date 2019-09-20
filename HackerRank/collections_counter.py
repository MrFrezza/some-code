from collections import Counter
qtd_shoes = int(input())

size_shoes = list(map(int, input().rstrip().split() ) )

count_shoes = Counter(size_shoes)

pagar = 0

for i in range(int(input())):
    inp = list(map(int, input().rstrip().split() ))
    if count_shoes[inp[0]] > 0:
        count_shoes[inp[0]] -= 1
        pagar += inp[1]

print(pagar)