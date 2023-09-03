import sys

#input
A, B, C, N = map(int, input().split())

result =0
maxNum = int(N / A)

for i in range(1,maxNum+1):
    for j in range(1,maxNum+1):
        for k in range(1,maxNum+1):
            sum = A*i + B*j + C*k
            if sum == N:
                result =1
                break

print(result)