import math
import os
import random
import re
import sys


def compara(strings, queries):
    
    conta = []
    ctr = 0
    for item in queries:
        conta.append(0)
        for x in strings:
            if item == x:
                conta[ctr] += 1
        ctr += 1
    return conta



string_count = int(input())
strings = []

for _ in range(string_count):
    string_item = input()
    strings.append(string_item)

queries_count = int(input())
queries = []

for _ in range(queries_count):
    query_item = input()
    queries.append(query_item)

print(compara(strings, queries))