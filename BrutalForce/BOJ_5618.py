import sys

#readline
data = []
for _ in range(2):
  line = sys.stdin.readline().rstrip()
  data.append(line)

n = int(data[0])
#number = list(map(int, data[1].split()))

#구현1  #시간 초과
# number = list(map(int, data[1].split()))
# m = min(number)

# for i in range(1, m+1):
#     if sum(list(map(lambda x: x%i, number)))== 0 :
#         print(i)

#구현2
if n==2:
    a,b = map(int, data[1].split())
    for i in range(1,min(a,b)+1):
        if a%i ==0 and b%i ==0:
            print(i)
if n==3:
    a,b,c = map(int, data[1].split())
    for i in range(1,min(a,b,c)+1):
        if a%i ==0 and b%i ==0 and c%i ==0:
            print(i)