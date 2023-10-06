N, M, V = map(int, input().split())

graph = [[False]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)

def dfs(idx):
    visited[idx] = True
    print(idx, end=' ')

    for i in range(1,N+1):
        if visited[i]==False and graph[idx][i]:
            dfs(i)

def bfs(V):
    q= [V]
    visited[V] = True

    while q:
        idx = q.pop(0)
        print(idx, end=' ')

        for i in range(1,N+1):
            if visited[i] == False and graph[idx][i]:
                q.append(i)
                visited[i] = True


for _ in range(M):
    x,y = map(int, input().split())
    graph[x][y] = graph[y][x] = True

dfs(V)
print()

visited = [False]*(N+1)
bfs(V)