#입력 초기화
N = int(input().rstrip())
graph = [ list(map(int, input().split())) for _ in range(N)]
visited = [ [False]*N for _ in range(N)]
answer = "Hing"

#함수 정의
def dfs(x,y):
    global answer

    visited[x][y] = True
    value = graph[x][y]

    #print("x,y",x,y,end=" ")
    #print("value", value, end="\n")
    
    if value < 0:
        answer = "HaruHaru"
        return

    if x + value < N:
        if visited[x+value][y] == False:
            dfs(x+value, y)

    if y + value < N:
        if visited[x][y+value] == False:
            dfs(x,y+value)

    return



#그래프 탐색
dfs(0,0)
print(answer)