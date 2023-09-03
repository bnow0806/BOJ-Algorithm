#input
N = int(input())

#풀이
#1. 1부터 N 까지 수를 분해합을 구한다.
#2. 분해합이 N인 경우 break한다.
#3. 분해합이 N이 안 나오는 경우 0출력

#구현
result = 0

for i in range(1,N+1):

    separatedI = list(map(int, str(i)))  
    sumI = i + sum(separatedI)

    if sumI == N :
        result = i
        break

print(result)