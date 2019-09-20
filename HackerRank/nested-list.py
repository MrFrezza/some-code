from operator import itemgetter

sala = []

tam = int(input())

for _ in range(tam):
    name = input()
    score = float(input())

    sala.append([name, score])

arrumado = sorted(sala, key=itemgetter(1))
b=1
n = []
c = True
while c and b < tam:
    if arrumado[0][1] != arrumado[b][1]:
        n.append(arrumado[b])
        if b < tam-1:
            if arrumado[b][1] == arrumado[b+1][1]:
                n.append(arrumado[b+1])
        c = False
    b += 1

arrumado = sorted(n,key=itemgetter(0))
for i in arrumado:
    print(i[0])

