n = int(input())

arr = [0]*1001
arr[1] = 1
arr[2] = 2

def dp(n):
    if arr[n]!=0:
        return arr[n]
    else:
        arr[n] = dp(n-1)+dp(n-2)
        return arr[n]

print(dp(n)%10007)