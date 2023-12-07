T = int(input())

dp = [[0] for _ in range(12)]
result = []

for _ in range(T):

    #찾으려는 횟수
    N = int(input())

    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    
    if dp[N] !=[0]:
        #print(dp[N])
        result.append(dp[N])
    else:
        for i in range(4,N+1):
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
        
        #print(dp[N])
        result.append(dp[N])

for res in result:
    #print("---")
    print(res)