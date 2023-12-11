T = int(input())

result = []
for _ in range(T):
    n = int(input())

    #2*n 행렬
    arr = [[0]*(n+1) for _ in range(2)]
    dp = [[0]*(n+1) for _ in range(2)]

    arr[0] = list(map(int, input().split()))
    arr[1] = list(map(int,input().split()))
    #print("arr[0]",arr[0])

    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    dp[0][1] = arr[1][0] + arr[0][1]
    dp[1][1] = arr[0][0] + arr[1][1]

    for i in range(2,n):
        dp[0][i] = max(dp[1][i-1],dp[1][i-2]) + arr[0][i]
        dp[1][i] = max(dp[0][i-1],dp[0][i-2]) + arr[1][i]

    result.append(max(dp[0][n-1], dp[1][n-1]))

#print(result)
for res in result:
    print(res)