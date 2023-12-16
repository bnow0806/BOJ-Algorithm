N= int(input().strip())

dp = [0]*(N+10)

dp[1] =1
dp[2] =1
dp[3] =2

if dp[N] !=0:
    print(dp[N])

else:
    for i in range(4,N+1):
        dp[i] = sum(dp[1:i-1]) +1

    print(dp[N])