N, M = map(int, input().split())

graph = [[False]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)
answer = 0

def bfs(x):
    q = [x]
    visited[x] = True

    while q:
        cur = q.pop(0)
        #print(cur, end=' ')

        for i in range(1,N+1):
            if visited[i] == False and graph[cur][i]:
                q.append(i)
                visited[i]= True


for _ in range(M):
    a,b = map(int, input().split())
    graph[a][b] = graph[b][a] = True

for x in range(1, N+1):
        if visited[x] == False:
            bfs(x)
            answer +=1
            #print()

print(answer)