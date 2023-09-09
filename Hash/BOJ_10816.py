N = int(input())
cards = input().split()
#print(cards)
M= int(input())
numbers = input().split()
#print(numbers)

answer = {}
for number in numbers:
    answer[number] = cards.count(number)


#출력
for key in answer.keys():
    print(answer[key], end=" ")
