M, N = map(int, input().split())

graph_W = [[0]*(M+2) for _ in range(N+2)]
graph_B = [[0]*(M+2) for _ in range(N+2)]
visited_W = [[0]*(M+2) for _ in range(N+2)]
visited_B = [[0]*(M+2) for _ in range(N+2)]

def bfs(y,x, graph, visited):

    q=[(y,x)]
    visited[y][x] = 1
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    ans =1

    while q:
        cur_y, cur_x = q.pop(0)

        for i in range(4):
            new_y = cur_y + dy[i]
            new_x = cur_x + dx[i]

            if graph[new_y][new_x] ==1 and visited[new_y][new_x] ==0:
                q.append((new_y,new_x))
                visited[new_y][new_x] =1
                ans +=1

    return ans

for i in range(N):
    line = input().strip()
    
    for j in range(M):
        if line[j] == 'W':
            graph_W[i+1][j+1] = 1
        else:
            graph_B[i+1][j+1] = 1

#print(graph_W)
#print(graph_B)

result_W = []
result_B = []
for y in range(1,N+1):
    for x in range(1,M+1):
        #print("bp1")
        if graph_W[y][x] ==1 and visited_W[y][x] ==0:
            #print(y,x,"y,x_W")
            ans = bfs(y,x,graph_W,visited_W)
            #print("W")
            result_W.append(ans)

for y in range(1,N+1):
    for x in range(1,M+1):
        #print("bp2")
        if graph_B[y][x] ==1 and visited_B[y][x] ==0:
            ans = bfs(y,x,graph_B,visited_B)
            #print("B")
            result_B.append(ans)

sum_W = 0
sum_B = 0
for W in result_W:
    sum_W += W**2

for B in result_B:
    sum_B += B**2

print(sum_W, sum_B)