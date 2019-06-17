import math
import os
import random
import re
import sys

n = int(input())
ar = list(map(int, input().rstrip().split()))

print(ar)

contador = {}
for i in ar:
    if i in contador:
        contador[i] += 1
    else:
        contador[i] = 1

print(contador)

final = 0
for c in contador:
    final += int(contador[c]/2)
    print(f' {c} :  {contador[c]} / 2 = {int(contador[c]/2)}')

print(f'Total de pares: {final}')