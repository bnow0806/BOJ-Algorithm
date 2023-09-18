N = int(input().rstrip())

hash_map = {}
for _ in range(N):
    name = input().rstrip()

    #중복 처리
    if name in hash_map:
        hash_map[name] +=1
    else:
        hash_map[name] =1

#print("hash_map",hash_map)

hash_map2 = {}
for _ in range(N-1):
    name2 = input().rstrip()

    #중복 처리
    if name2 in hash_map2:
        hash_map2[name2] +=1
    else:
        hash_map2[name2] =1

#print("hash_map2",hash_map2)

for key in hash_map.keys():
    if key not in hash_map2:
        print(key)
        break
    else:
        if hash_map[key] != hash_map2[key]:
            print(key)
            break