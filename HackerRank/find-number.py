import math
import os
import random
import re
import sys


def findNumber(arr, k):
    for i in arr:
        if i == k:
            return 'YES'

    return 'NO'

arr_count = int(input().strip())

arr = []

for _ in range(arr_count):
    arr_item = int(input().strip())
    arr.append(arr_item)

k = int(input().strip())

print(findNumber(arr, k))