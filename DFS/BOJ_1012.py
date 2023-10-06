import sys
sys.setrecursionlimit(100000)

T = int(input().rstrip())

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [ [0]*N for _ in range(M)]
    visited = [ [False]*N for _ in range(M)]
    each = 0
    result = []

    #함수
    def dfs(x,y):
        global each
        dx = [-1, 1, 0 ,0]  #상하좌우
        dy = [ 0, 0, -1, 1] 

        #동작
        visited[x][y] = True
        each +=1

        for i in range(0,4):
            new_x = x+dx[i]
            new_y = y+dy[i]
            if new_x < 0 or new_x >= M or new_y <0 or new_y >=N:
                continue
            
            if graph[new_x][new_y] and not visited[new_x][new_y]:
                dfs(new_x, new_y)

        return

    #초기화
    for _ in range(K):
        a, b = map(int, input().split())
        graph[a][b] = 1


    #그래프 탐색
    for x in range(M):
        for y in range(N):
            if graph[x][y] and visited[x][y] == False:
                dfs(x,y)
                if each !=0:
                    result.append(each)
                    each = 0

    #print(result)
    print(len(result))