import math
import os
import random
import re
import sys

nd = input().split()
n = int(nd[0])
d = int(nd[1])

a = list(map(int, input().rstrip().split()))

print(a)

for i in range(d):
    tempp = a[0]
    del a[0]
    a.append(tempp)

print("----------")
print(a)