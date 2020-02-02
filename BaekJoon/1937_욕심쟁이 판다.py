import sys
sys.stdin = open('1937_input.txt')


def Panda(i, j):
    visited[i][j] = 1
    for idx in range(4):
        x = i + dx[idx]
        y = j + dy[idx]
        if x < 0 or x >= N or y < 0 or y >= N: continue
        if Bamboo[x][y] > Bamboo[i][j]:
            if visited[x][y]:
                return visited[x][y]
            else:
                rst = Panda(x, y)
            if visited[i][j] < visited[i][j] + rst:
                visited[i][j] =  visited[i][j] + rst
    return 1


N = int(input())
Bamboo = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
visited = [[0 for _ in range(N)] for _ in range(N)]
rst = []

for i in range(N):
    for j in range(N):
        Panda(i, j)

print(visited)

maxx = 1
for i in range(N):
    if maxx < max(visited[i]):
        maxx = max(visited[i])

print(maxx)
