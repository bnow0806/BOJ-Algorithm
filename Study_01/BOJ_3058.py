T = int(input())

for _ in range(T):
    number = list(map(int, input().split()))

    evenNumber = []
    for num in number:
        if num %2 ==0:
            evenNumber.append(num)
    
    print(sum(evenNumber),min(evenNumber))