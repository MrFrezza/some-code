mes = input()

final = ''

for i in range(len(mes)):
    if i < len(mes)-1:
        if mes[i+1] == mes[i]:
            final += mes[i] + str(1)
        else:
            final += mes[i] + str(0)
    else:
        final += mes[i] + str(0)


f1 = list(final)
temp = ''

tamanho = len(f1)

i = 0
tpp = 0
pts = 0
while i < tamanho:
    if i+2 < tamanho:
        if f1[i] == f1[i+2]:
            next = True
            tpp = i+2
            pts += 1
            while next:
                # tpp = int(f1[i+1]) + int(f1[i+3])
                if tpp+2 < tamanho:
                    if f1[tpp] == f1[tpp + 2]:
                        pts += 1
                        tpp += 2
                    else:
                        next = False
                else:
                    next = False
            
            temp += f1[i] + str(pts)
            i = i + tpp
            if i > tamanho:
                break
        else:
            temp += str(f1[i])
    else:
        temp += str(f1[i])
    i += 2


print(final)
print(f1)
print(temp)