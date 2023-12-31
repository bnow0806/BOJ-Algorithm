N = int(input())

dp = [[0]*10 for _ in range(N+1)]

for k in range(0,10):
    dp[1][k] = 1


for n in range(2,N+1):
    for k in range(0,10):
        for l in range(k,10):
            dp[n][k] += dp[n-1][l]

#print(dp)
sum = 0
for k in range(0,10):
    sum += dp[N][k]

print(sum%10007)