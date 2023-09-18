N = int(input().rstrip())
M = int(input().rstrip())

graph = [[False]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)
answer = 0

def dfs(idx):
    global answer

    visited[idx] = True
    answer = answer+1
    for i in range(1,N+1):
        if visited[i] == False and graph[idx][i]:
            dfs(i)

# 그래프 정보 입력
for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = True

# dfs 및 결과 출력
dfs(1)

print(answer-1)
