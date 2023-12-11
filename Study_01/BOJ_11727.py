N=int(input())

arr = [0]*(10**3+1)

arr[1] =1
arr[2] =3

for i in range(3,N+1):
    arr[i] = arr[i-1]+arr[i-2]*2

print(arr[N]%10007)