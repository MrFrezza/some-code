def reverseArray(arr):
    # Cria uma copia In-Place usando SLICE, mas ocupa mais espaço
    return arr[::-1]

arr_count = int(input())

arr = list(map(int, input().rstrip().split()))

print(reverseArray(arr))