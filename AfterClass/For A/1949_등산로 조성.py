import sys
sys.stdin = open('1949_input.txt')

def pprint(arr):
    for i in range(len(arr)):
        print(arr[i])


def FindTrail(x, y):
    global visitmax
    visited[x][y] += 1
    if visited[x][y] > visitmax:
        visitmax = visited[x][y]

    for idx in range(4):
        a = x + dx[idx]
        b = y + dy[idx]
        if a < 0 or a > N - 1 or b < 0 or b > N - 1: continue
        if MAP[a][b] >= MAP[x][y]: continue
        if visited[a][b] == 0:
            visited[a][b] += visited[x][y]
            FindTrail(a, b)
            visited[a][b] = 0   # 리셋(클리어)


for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    visitmax = 0

    starts = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    maxx = 0
    for i in range(N):
        for j in range(N):
            if MAP[i][j] > maxx:
                maxx = MAP[i][j]

    for i in range(N):
        for j in range(N):
            if MAP[i][j] == maxx:
                starts.append([i, j])

    for k in range(1, K + 1):
        for i in range(N):
            for j in range(N):
                MAP[i][j] -= k
                for start in starts:
                    visited = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
                    x, y = start
                    FindTrail(x, y)
                MAP[i][j] += k

    print("#{} {}".format(tc, visitmax))