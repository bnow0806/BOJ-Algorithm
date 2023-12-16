import itertools

arr = []
result = []

for _ in range(9):
    arr.append(int(input().rstrip()))

nCr = itertools.combinations(arr,7)

#print(list(nCr))

for ncr in list(nCr):
    if sum(ncr) == 100:
        result = list(ncr)
        break

result.sort()
#print("result", result)

for res in result:
    print(res)