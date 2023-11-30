import sys
from collections import deque

def bfs(startX, endX):
    global visited

    if startX == endX:
        return 0

    q = deque([startX])
    visited[startX] = True
    ans = 1

    while q:
        size = len(q)
        #print("---",ans,"step","---")
        #1단계, 2단계... queue를 털때 마다 s번 반복 및 ans +1
        for s in range(size):
            x = q.popleft()
            #print("x:",x)
            for i in range(3):
                match i:
                    case 0:
                        nx = x-1
                    case 1:
                        nx = x+1
                    case 2:
                        nx = x*2
                #print("nx:",nx)
                if nx == endX:
                    return ans

                elif 0 <= nx <= MAX and not visited[nx]:
                    visited[nx] = True
                    q.append(nx)

        ans += 1

    return ans

startX, endX = map(int, input().split())

MAX = 100000
visited = [False] * (MAX+1)

print(bfs(startX, endX))