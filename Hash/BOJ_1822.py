nA , nB = map(int, input().split())

A = list(input().split())
B = list(input().split())

hash_map = {}
for b in B:
    hash_map[b] = 1

commonValue = []
for a in A:
    if a in hash_map:
        commonValue.append(a)

#print("commonValue", commonValue)
if len(commonValue) == nA:  #모두 중복이라면
    print(0)
else:   #일부 중복이라면
    for cValue in commonValue:
        A.remove(cValue)

    print(len(A))
    A = list(map(int, A))
    A.sort  #작은수 부터 출력
    for i in range(0,len(A)):
        print(A[i], end=" ")