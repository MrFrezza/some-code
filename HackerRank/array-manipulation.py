from timeit import default_timer as timer

# Não é recomendado para INPUTS grandes
def arrayManipulation(n, queries):
    arr = [0] * n
    comp = 0
    for i in queries:
        for j in range((i[0]-1), i[1] ):
            arr[j] += i[2]
    
    for j in range(n):
        if comp < arr[j]:
            comp = arr[j]
    
    return comp

# Este método é otimizado
def optOutra(n, queries):
    arr = [0] * (n+1)
    comp = 0

    for i in queries:
        arr[i[0]-1] += i[2]
        arr[ i[1] ] += -i[2]    

    for i in range(1, n+1):
        arr[i] = arr[i] + arr[i-1]
        if arr[i-1] > comp:
            comp = arr[i-1]
    
    return comp

nm = input().split()

n = int(nm[0])
m = int(nm[1])

queries = []

for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))

start = timer()
print(arrayManipulation(n, queries))
print(f'Tempo 1: {timer() - start}')

start = timer()
print(optOutra(n, queries))
print(f'Tempo 2: {timer() - start}')
