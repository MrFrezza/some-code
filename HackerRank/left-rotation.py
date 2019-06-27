nd = input().split()
n = int(nd[0])
d = int(nd[1])

a = list(map(int, input().rstrip().split()))
final = ""

for i in range(d):
    tmp = a[0]
    del a[0]
    a.append(tmp)

for i in a:
    final = final + str(i) + ' '

print(final.strip())