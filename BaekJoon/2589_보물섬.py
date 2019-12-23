import sys
sys.stdin = open('2589_input.txt')

import collections


def BFS(i, j):
    global maxx
    q.append((i, j))
    visited[i][j] = 0
    while q:
        x, y = q.popleft()
        for idx in range(4):
            a = x + dx[idx]
            b = y + dy[idx]
            if a < 0 or a >= N or b < 0 or b >= M: continue
            if visited[a][b] != -1 or MAP[a][b] != 'L': continue
            visited[a][b] = visited[x][y] + 1
            if visited[a][b] > maxx:
                maxx = visited[a][b]
            q.append((a, b))


N, M = map(int, input().split( ))
MAP = [list(input()) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = collections.deque()
maxx = 0

for i in range(N):
    for j in range(M):
        if MAP[i][j] == 'L':
            visited = [[-1 for _ in range(M)] for _ in range(N)]
            BFS(i, j)

print(maxx)
