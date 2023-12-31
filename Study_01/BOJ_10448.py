T = int(input())
result = []

number = []
for _ in range(T):
    number.append(int(input()))    #10,20,1000

Tn = []
for n in range(1,45):
    Tn.append(int(n*(n+1)/2))

#print(Tn)

for num in number:
    answer = 0
    for Ti in Tn:
        if answer ==1:
            break
        for Tj in Tn:
            if answer ==1:
                break
            for Tk in Tn:
                if num == Ti+Tj+Tk:
                    #print("num == Ti+Tj+Tk",Ti,Tj,Tk)
                    answer = 1
                    break

    result.append(answer)

for res in result:
    print(res)

