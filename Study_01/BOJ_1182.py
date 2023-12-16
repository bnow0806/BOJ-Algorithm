import itertools

N, S = map(int, input().split())
arr = list(map(int, input().split()))

#print(arr)

count = 0
for i in range(1,N+1):
    nCr = itertools.combinations(arr,i)

    for ncr in list(nCr):
        if sum(ncr) == S:
            count +=1
    
    nCr = []

print(count)