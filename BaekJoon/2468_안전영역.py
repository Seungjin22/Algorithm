import sys
sys.stdin = open('2468_input.txt')
import collections

def BFS(x, y, k):
    global visit
    q.append([x, y])
    visited[x][y] = visit
    while q:
        x, y = q.popleft()
        for idx in range(4):
            a = x + dx[idx]
            b = y + dy[idx]
            if a < 0 or a >= N or b < 0 or b >= N: continue
            if area[a][b] <= k: continue
            if visited[a][b] != 0: continue
            q.append([a, b])
            visited[a][b] = visit

N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
q = collections.deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
visit = 0
top = 0
maxx = 1

for i in range(N):
    if max(area[i]) > top:
        top = max(area[i])

for k in range(1, top):
    for i in range(N):
        for j in range(N):
            if area[i][j] > k and visited[i][j] == 0:
                visit += 1
                BFS(i, j, k)
    if visit > maxx:
        maxx = visit
    visit = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]

print(maxx)