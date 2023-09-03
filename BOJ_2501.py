import sys

#input
N, K = map(int, input().split())

#풀이
#1. 1~N 까지 수를 N 으로 나눠본다.
#2. 나머지가 0 이면 배열에 담는다.
#3. 배열의 K-1번째를 출력한다.
#4. 배열 크기가 K 보다 작다면 0을 출력한다.

array = []

for i in range(1,N+1):
    if (N % i == 0):
        array.append(i)

if len(array)<K:
    print(0)
    #print("len(array) :"+str(len(array)))
else:
    print(array[K-1])
