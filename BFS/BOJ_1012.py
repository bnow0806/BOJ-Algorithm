T= int(input())
for _ in range(T):

    M, N, K = map(int, input().split())

    graph = [[0]*(M+1) for _ in range(N+1)]
    visited = [[False]*(M+1) for _ in range(N+1)]

    answer = 0

    def bfs(y,x):
        q = [(y,x)]
        visited[y][x] = True

        dy = [ 0, 0, -1, 1]
        dx = [-1, 1, 0 ,0]
        
        while q:
            (cur_y,cur_x) = q.pop(0)

            for i in range(0,4):
                new_y = cur_y+dy[i]
                new_x = cur_x+dx[i]

                if graph[new_y][new_x] and visited[new_y][new_x]==False:
                    q.append((new_y,new_x))
                    visited[new_y][new_x] = True


    for _ in range(K):
        a, b = map(int, input().split())
        graph[b][a] = 1


    for x in range(0,M+1):
        for y in range(0,N+1):
            if graph[y][x] == 1 and visited[y][x] == False:
                bfs(y,x)
                answer +=1
                print("x,y: ",x,y)

    print(answer)