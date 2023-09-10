T = int(input().rstrip())

for _ in range(T):
    N = input().rstrip()
    nList = list(map(int,input().split()))
    M = input().rstrip()
    mList = list(map(int,input().split()))

    hash_map1 = {}
    for n in nList:
        hash_map1[n] = 1

    hash_map2 = {}
    for m in mList:
        if m in hash_map1:
            print(1)
        else:
            print(0)