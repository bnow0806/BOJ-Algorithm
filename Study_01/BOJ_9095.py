T = int(input())

dp = [[0] for _ in range(12)]
result = []

for _ in range(T):

    #찾으려는 횟수
    N = int(input())

    dp[1] = 0
    dp[2] = 1
    dp[3] = 3
    dp[4] = 7
    dp[5] = 13
    dp[6] = 24
    
    if dp[N] !=[0]:
        #print(dp[N])
        result.append(dp[N])
    else:
        for i in range(7,N+1):
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
        
        #print(dp[N])
        result.append(dp[N])

for res in result:
    #print("---")
    print(res)