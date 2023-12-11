import sys
sys.setrecursionlimit(10**6)

N = int(input())

#2~10**6
arr = [0]*(10**6+1)
result = 0

arr[2]=1
arr[3]=1


if arr[N]!=0:
    result = arr[N]

else:
    for i in range(4,N+1):
        if i %6 ==0:
            arr[i] = min(arr[i//2],arr[i//3]) + 1
        elif i %3 ==0 :
            arr[i] = min(arr[i//3],arr[i-1]) + 1
        elif i %2 ==0 :
            arr[i] = min(arr[i//2],arr[i-1]) + 1
        else:
            arr[i] = arr[i-1] + 1
    
    result = arr[N]
    
print(arr[N])