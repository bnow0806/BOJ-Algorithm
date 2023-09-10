# 풀이
#1. n개중 k 개 선택, 순서 포함
#2. 합친 후, hash에 저장

import itertools

n = int(input().rstrip())
k = int(input().rstrip())

number = []
for _ in range(n):
    number.append(input().rstrip())


nPr = itertools.permutations(number, k)

hash_map = {}

for tuple in nPr:
    value = tuple[0]
    for i in range(1,k):
        value += tuple[i]

    if value not in hash_map:
        hash_map[value] =1

print(len(hash_map))