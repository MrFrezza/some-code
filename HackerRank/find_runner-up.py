n = int( input() )
arr = set(input().split())

a = list(arr)
arr = [int(x) for x in a]
arr.sort()
print(arr)
print(arr[-2])