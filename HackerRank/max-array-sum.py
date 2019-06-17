import math
import os
import random
import re
import sys

import pprint

def maxSubset(arr):
    tab = {}
    tam = len(arr)
    for i in range(tam):
        tmp = arr[i]
        for j in range(i+2, tam):
            print(str(tmp) + ' ' +str(arr[j]))
            tab[str(tmp)+str(arr[j])] = tmp + arr[j]

    pprint.pprint(tab)
    
        



if __name__ == '__main__':
    #n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubset(arr)
    #print(res)