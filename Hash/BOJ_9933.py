N = int(input())

hash_map = {}
for _ in range(N):
    name = input()
    hash_map[name] = 1

#print(hash_map)

answer = ""
for key in hash_map.keys():
    reverse_key = key[::-1]
    #print(reverse_key)
    if reverse_key in hash_map:
        answer = reverse_key

#print("answer ",answer)
print(len(answer), end=" ")

index = len(answer)//2
print(answer[index])
    
    

