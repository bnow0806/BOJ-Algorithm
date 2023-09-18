N, M = map(int, input().split())
graph = [ input() for _ in range(N)]
visited = [[False]*M for _ in range(N)]

each = 0
result = []

def dfs(x,y):
    global each

    each +=1
    visited[x][y] = True

    #print("x,y",x,y, end=" ")
    #print(graph[x][y], end="\n")
    old = graph[x][y]
    if  y+1 <M and graph[x][y] == '-':
        y = y+1
    elif x+1 <N and graph[x][y] == '|':
        x = x+1
    else:
        return  #x,y 범위 넘어갈 때

    if visited[x][y] == False and graph[x][y] == old:
        dfs(x,y)
    
    return

for x in range(N):
    for y in range(M):
        if visited[x][y] == False:
            dfs(x,y)
            result.append(each)
            each = 0

#print(result)
print(len(result))