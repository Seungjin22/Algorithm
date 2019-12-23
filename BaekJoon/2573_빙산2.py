import sys
sys.stdin = open('2573_input.txt')

import collections

def BFS(x, y):
    global visit
    q.append((x, y))
    visited[x][y] = visit
    while q:
        x, y = q.popleft()
        for idx in range(4):
            a = x + dx[idx]
            b = y + dy[idx]
            if a < 0 or a >= N or b < 0 or b >= M: continue
            if SEA[a][b] == 0:
                melted[x][y] += 1
            if SEA[a][b] == 0: continue
            if visited[a][b] != 0: continue
            q.append((a, b))
            visited[a][b] = visit


N, M = map(int, input().split())
SEA = [list(map(int, input().split())) for _  in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
melted = [[0 for _ in range(M)] for _ in range(N)]
q = collections.deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visit = 0
year = 0


points = []
for i in range(N):
    for j in range(M):
        if SEA[i][j] > 0:
            points.append((i, j))

while True:
    for point in points:
        i, j = point
        if visited[i][j] == 0:
            visit += 1
            BFS(i, j)
    if visit >= 2: break
    visit = 0
    visited = [[0 for _ in range(M)] for _ in range(N)]

    for point in points:
        i, j = point
        if SEA[i][j] < melted[i][j]:
            SEA[i][j] = 0
        else:
            SEA[i][j] -= melted[i][j]
        if SEA[i][j] == 0:
            points.remove((i, j))

    melted = [[0 for _ in range(M)] for _ in range(N)]
    year += 1

if visit == 1:
    year = 0

print(year)