import sys
sys.stdin = open('2667_input.txt')


def DFS(x, y):
    global visit
    global cnt
    s.append((x, y))
    while s:
        x, y = s.pop(-1)
        if not visited[x][y]:
            visited[x][y] = visit
            cnt += 1
            for idx in range(4):
                a = x + dx[idx]
                b = y + dy[idx]
                if a < 0 or a >= N or b < 0 or b >= N: continue
                if MAP[a][b] == 1 and visited[a][b] == 0:
                    s.append((a, b))



N = int(input())
MAP = [list(map(int, input())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
s = []
rst = []
visit = 0
cnt = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(N):
        if MAP[i][j] == 1 and visited[i][j] == 0:
            visit += 1
            DFS(i, j)
            rst.append(cnt)
            cnt = 0

print (visit)
for r in sorted(rst):
    print(r)
