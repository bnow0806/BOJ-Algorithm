import sys
import math

#input
P, K = map(int, input().split())

#풀이
#1. P 이하 소수 찾기
#2. K 이하 소수 중 가장 큰 2개곱 보다 클시, GOOD
#3. K 이하 소수 중 가장 큰 2개곱 보다 작을시, BAD
#4. 소수 2개를 골라 곱해가면 맞는지 확인, p 반환

def isPrime(n):
    
    for i in range (2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False  
    return True

# 구현 #
primeNumber = []
pq = []

for i in range(2,P):
    if isPrime(i) == True:
        primeNumber.append(i)

primeNumberLength = len(primeNumber)
for i in range(0, primeNumberLength):
    for j in range(0, primeNumberLength):
        if primeNumber[i] * primeNumber[j] == P:

            pq.append(primeNumber[i])

            if(len(pq)==2):
                #print("len(pq)==2")
                break;

if pq[0] > K:
    print("GOOD")
else:
    print("BAD "+str(pq[0]))