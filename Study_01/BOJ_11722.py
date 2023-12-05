N = int(input())

# arr 0, 1, 2, 3, 4, 5
arr = list(map(int, input().split(" ")))

dp = [1]*(N)

for i in range(1,N):
    for j in range(0,i):
        if arr[j] > arr[i]:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp))