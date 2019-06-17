import math
import os
import random
import re
import sys


def soma(arr):
    v_1 = 0
    t = []
    tam = len(arr)
    
    for i in range(1, tam+1):
        for j in range(i):
            t.append( [ a for a in arr[j:i] ]   )
            v_1 += sum(t[-1])

    
    #print(v_1)
    return v_1

arr_count = int(input().strip())

arr = []

for _ in range(arr_count):
    arr_item = int(input().strip())
    arr.append(arr_item)

print(soma(arr))