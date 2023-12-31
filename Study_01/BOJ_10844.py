N = int(input())

# dp = [ [set([]) for _ in range(10)] for _ in range(N+1)]

# for k in range(1,10):
#     dp[1][k].add(k)

# for n in range(2,N+1):
#     for k in range(1,10):
#         for num in dp[n-1][k]:
#             last = num % 10
#             if (10**(n-1)) <= (num*10+(last-1)):
#                 dp[n][k].add(num*10+(last-1))
#             if (num*10+(last+1)) < (10**n) :
#                 dp[n][k].add(num*10+(last+1))

# k로 끝나는 자리 기준으로 풀기
dp = [[0]*10 for _ in range(N+1)]

for k in range(1,10):
    dp[1][k]=1

for n in range(2,N+1):
    dp[n][0] = dp[n-1][1]
    dp[n][9] = dp[n-1][8]
    for k in range(1,9):
        dp[n][k] = dp[n-1][k-1] + dp[n-1][k+1]

# for n in range(0,N+1):
#    print(dp[n])

print(sum(dp[N])%1000000000)