import math
import os
import random
import re
import sys

n = int(input())
c = list(map(int, input().rstrip().split()))

l = []

for i in range(n):

    if c[i] != 1:
        if (i+1) <= n-1:
            v_p = (i+1 if c[i+1] == 0 else -1)
            if (i+2) <= n-1:
                v_s = (i+2 if c[i+2] == 0 else -1)
        
        l.append( [i, [v_p, v_s] ] )

for i in l:
    print(i)

print("------")

fila = [0]
pulo = 0
for j in fila:    
    for i in l[ j ][1]:
        if i != -1 and not(i in fila):
            fila.append(i)
            pulo += 1

    
    del fila[0]

print(pulo)
