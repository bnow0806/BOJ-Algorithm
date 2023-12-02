n = int(input())

# DP 값 저장 리스트
# COST 값 저장 리스트(입력)
# N*3
dp = [[0]*3 for _ in range(n)]
arr = [[0]*3 for _ in range(n)]

for i in range(n):
    arr[i][0], arr[i][1], arr[i][2] = map(int, input().split())


print(arr)

dp[0][0] = arr[0][0]
dp[0][1] = arr[0][1]
dp[0][2] = arr[0][2]

for i in range(1,n):
    print("i", i)
    dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + arr[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + arr[i][1]
    dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + arr[i][2]

print(min(dp[n-1]))