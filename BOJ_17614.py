import sys

#input
N = int(input())
#print(N)

K=0

#풀이
#1. 1부터 N 까지 숫자중에 3,6,9가 있는지 확인
#2. 2자리 수라면, 2번 등록
#3. 숫자 합을 출력한다.

for i in range(1,N+1):

    num_list = list(map(int, str(i)))
    #print("len(num_list) : "+str(len(num_list)))

    for j in range(0,len(num_list)):
        if num_list[j] % 3 == 0 and num_list[j]>0:
            #print("num_list[j] : "+str(num_list[j]))
            K+=1

print(K)