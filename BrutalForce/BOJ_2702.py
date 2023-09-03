import sys

#readline
datas = []
while True:
  try:
    line = input()
    if line == "":
        break
    datas.append(line)
  except:
    break

#print(datas)

#a , b = map(int, input().split())

#풀이
#1. b 부터 시작해서 a 배수까지 늘려간다음에, 최소 공배수를 찾는다.
#2. a 에서 배려가면서, a 와 b 를 모두 나눌수 있는, 최대 공약수를 찾는다.

#구현
def printResult (a , b):
    result = []

    for i in range(1, a+1):
        if (b*i) % a ==0:
            #print ("b*i", b*i)
            result.append(b*i)
            break

    for i in range(a, 0, -1):
        if a % i ==0 and b % i ==0:
            #print ("i", i)
            result.append(i)
            break

    print(result[0],result[1])


for data in datas:
    try:
        a , b = map(int, data.split(" "))
        printResult(a, b)
    except:
       pass

