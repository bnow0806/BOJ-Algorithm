N= int(input().strip())

dp = [0]*(N+10)

dp[1] =1
dp[2] =2
dp[3] =3

if dp[N] !=0:
    print(dp[N])

else:
    for i in range(4,N+1):
        dp[i] = (2*dp[i-2]+dp[i-3])%15746

    print(dp[N])