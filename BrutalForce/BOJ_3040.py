import sys
from itertools import combinations, permutations

#readline
data = []
for i in range(9):
  line = sys.stdin.readline().rstrip()
  data.append(line)
  
#print("data1",data)

#풀이
#1. 9개의 입력을 data 에 저장한다.
#2. 9개중 7개를 고르는 콤비네이션을 만든다.
#3. 합이 100이 되는 콤비네이션을 차례로 출력한다.

#구현
data = list(map(int, data))
#print("data2",data)
combinationList =combinations(data, 7)
#print(type(combinationList))

results = []

for combi in combinationList:
  #print("Debug1",combi,type(combi))
  if sum(combi) == 100:
    results = combi
    break
  
for result in results:
  print(result)
