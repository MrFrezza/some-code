import math
import os
import random
import re
import sys

def impar(l,r):
    arr = []
    for i in range(l,r+1):
        if (i % 2) != 0:
            arr.append(i)
    return arr


l = int(input().strip())
r = int(input().strip())

print(impar(l, r))