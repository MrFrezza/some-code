import math
import os
import random
import re
import sys

def beautifulSubarrays(a, m):
    impar = [ i for i in a if (i%2) != 0]
    t = []
    tam = len(a)
    
    if m > impar:
        return 0
    else:
        for i in range(1, tam+1):
            for j in range(i):
                t.append( [ b for b in a[j:i] ]   )
    print(t)
    return len(t)


a_count = int(input().strip())

a = []

for _ in range(a_count):
    a_item = int(input().strip())
    a.append(a_item)

m = int(input().strip())

result = beautifulSubarrays(a, m)
#print(result)