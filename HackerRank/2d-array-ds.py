import math
import os
import random
import re
import sys


arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

resps = []
total = 0

for l in range(len(arr) - 2 ):
    for c in range(len(arr) - 2 ):
        total += arr[l][c] + arr[l][c+1] + arr[l][c+2]
        total += arr[l+1][c+1]
        total += arr[l+2][c] + arr[l+2][c+1] + arr[l+2][c+2]
        resps.append(total)
        total = 0

resps.sort(reverse=True)
print(resps[0])
