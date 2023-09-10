#풀이
#1. 숫자를 key로 hash_map을 만든다.
#2. value 1순위, key 2순위로 정렬

N = int(input().rstrip())

hash_map = {}
for _ in range(N):
    name = int(input().rstrip())
    if name in hash_map:
        hash_map[name] +=1
    else:
        hash_map[name] =1
#print(hash_map)

sorted_list = sorted(hash_map.items(), key = lambda x:(-x[1],x[0]) )
print(sorted_list[0][0])

