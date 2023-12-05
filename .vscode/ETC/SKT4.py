import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dirY = [1, -1, 0, 0]
dirX = [0, 0, 1, -1]

def dfs(y, x, current_idx):
    global visited, board1, total, start, end, foundAnswer

    if foundAnswer:
        return
    
    visited[y][x] = current_idx

    # 정답 처리부
    if y == end[current_idx][0] and x == end[current_idx][1]:
        if current_idx + 1 == total:
            foundAnswer = True
            return
        dfs(start[current_idx + 1][0], start[current_idx + 1][1], current_idx + 1)
    
    if foundAnswer:
        return
    
    for i in range(4):
        newY = y + dirY[i]
        newX = x + dirX[i]
        if board1[newY][newX] != '#' and visited[newY][newX] == -1:
            dfs(newY, newX)

    if foundAnswer:
        return
    
    visited[y][x] = -1

# 0. 입력 및 초기화
N = int(input())
MAX = 10 + 10

# 1. map에 연결 정보 채우기
board1 = [[False] * (MAX) for _ in range(MAX)]
board2 = [[False] * (MAX) for _ in range(MAX)]
visited = [[-1] * MAX for _ in range(MAX)]

start = []
end = []

# make board1
for i in range(1, N + 1):
    row = input()
    for j in range(1, N + 1):
        if row[j - 1] != '#':
            board1[i][j] = True
            if row[j - 1].isalpha():
                if len(start) == len(end):
                    start.append((i, j))
                else:
                    end.append((i, j))

# make board2
for i in range(1, N + 1):
    row = list(map(int, input().split()))
    for j in range(1, N + 1):
        board2[i][j] = row[j - 1]


# 2. DFS 호출
total = len(start)
foundAnswer = False
dfs(start[0][0], start[0][1], 0)

if foundAnswer:
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if visited[i][j] != -1:
                print(board2[i][j], end = ' ')
            else:
                print(0, end = ' ')
        print()