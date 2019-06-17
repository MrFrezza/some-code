import math
import os
import random
import re
import sys


def meanderingArray(unsorted):
    ret = []
    unsorted.sort(reverse=True)
    
    c = 0
    f = len(unsorted)-1
    for i in range(len(unsorted)):
        if (i % 2) == 0:
            ret.append(unsorted[c])
            c += 1
        else:
            ret.append(unsorted[f])
            f -= 1
        
        if c > f:
            break

    return ret



unsorted_count = int(input().strip())

unsorted = []

for _ in range(unsorted_count):
    unsorted_item = int(input().strip())
    unsorted.append(unsorted_item)

result = meanderingArray(unsorted)
print(result)