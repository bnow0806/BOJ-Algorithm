N, M, K = map(int, input().split())

#상하좌우로 padding +2
graph = [[0]*(M+2) for _ in range(N+2)]
visited = [[0]*(M+2) for _ in range(N+2)]

#bfs 정의
def bfs(y,x):

    #q 초기화
    q=[(y,x)]
    visited[y][x]=1
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    ans=1

    #이동하면서 deque and enque
    while q:
        cur_y, cur_x = q.pop(0)

        for i in range(4):
            new_y = cur_y + dy[i]
            new_x = cur_x + dx[i]

            #print("new_y, new_x", new_y, new_x)

            if graph[new_y][new_x]==1 and visited[new_y][new_x]==0:
                q.append((new_y,new_x))
                visited[new_y][new_x] =1
                ans+=1
    return ans

# 그래프 초기화
for _ in range(K):
    a, b = map(int, input().split())
    graph[a][b] = 1

# bfs 전체 돌기
result = []
for y in range(1,N+1):
    for x in range(1,M+1):
        if graph[y][x] ==1 and visited[y][x]==0:
            ans = bfs(y,x)
            result.append(ans)


print(max(result))