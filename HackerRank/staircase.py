qtd = int(input())

hor = qtd-1

for i in range(1, qtd+1):
    p1 = ' ' * hor
    p2 = '#' * i
    print(p1+p2)
    hor -= 1
    

