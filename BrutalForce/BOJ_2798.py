import sys
from itertools import combinations, permutations

#readline
data = []
for i in range(2):
  line = sys.stdin.readline().rstrip()
  data.append(line)
  
#print(data)

#input
N, M = map(int, data[0].split())
cardList = list(map(int, data[1].split()))

#print(N, M)        #5 21
#print(cardList)    #5,6,7,8,9

#풀이
# N : 카드의 총 장수, M : 만들어야되는 숫자
# cardList : 카드 목록
# 1. 카드 목록 중 3개를 더해 만들 수 있는 숫자의 배열을 만든다.
# 2. M과 차이를 저장한다.
# 3. M과 차이가 양수이면서, 가장 작은 값의 인덱스를 얻는다.
# 4. 얻은 인덱스의 값을 리턴한다.

#구현
combinationList = list(combinations(cardList, 3))
sumCombiList = []
calSumCombiList = []

#print("combinationList :" , combinationList)

for  combination in combinationList:
  sumCombiList.append(sum(combination))

#print("sumCombiList :" , sumCombiList)

for i in range(0, len(sumCombiList)):
  if sumCombiList[i] <= M:
    calSumCombiList.append(M - sumCombiList[i])
  else:
    calSumCombiList.append(M)

minIndex = calSumCombiList.index(min(calSumCombiList))

#print("minIndex",minIndex)
print(sumCombiList[minIndex])