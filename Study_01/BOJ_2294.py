N, K = map(int, input().split())

coin = []
dp = [10001]*(K+10)

for _ in range(N):
    coin.append(int(input().rstrip()))

dp[0]=0
for i in range(1,K+1):
    for j in coin:

        #print("j",j)
        if j > i:
            continue
        #print("j <= i",j,i)
        dp[i] = min(dp[i],dp[i-j]+1)
        #print("i",i,"dp[i]",dp[i])

if dp[K] == 10001: print(-1)
else : print(dp[K])
    