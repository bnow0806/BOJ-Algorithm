#풀이
#1. 이름 enter 이면 추가
#2. 이름 leave 이면 빼기
#3. 이름 역순으로 출력

N = int(input())

hash_map = {}
for _ in range(N):
    M, K = map(str, input().split())
    if K =="enter":
        hash_map[M] = 1
    elif K =="leave":
        hash_map[M] = 0
    else:
        pass

list = []
for key in hash_map:
    if hash_map[key] ==1:
        list.append(key)

list.sort(reverse=True)

for item in list:
    print(item,end="\n")
