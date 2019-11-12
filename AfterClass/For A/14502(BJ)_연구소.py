import sys
sys.stdin = open('input.txt')


def pprint(arr):
    for i in range(len(arr)):
        print(arr[i])

def Virus(i,j):
    visited[i][j] = 1
    for idx in range(4):
        a = i + dx[idx]
        b = j + dy[idx]
        if a < 0 or a >= N or b < 0 or b >= M: continue
        if MAP[a][b] == 0 and visited[a][b] == 0:
            MAP[a][b] = 2
            Virus(a, b)


def dfs(wall, idx):
    global rst
    global cnt
    global maxx
    if wall == 3:
        for i in range(N):
            for j in range(M):
                if MAP[i][j] == 0:
                    if W[cnt]:
                        MAP[i][j] = 1
                    cnt += 1

        for i in range(N):
            for j in range(M):
                if MAP[i][j] == 2:
                    Virus(i, j)

        for i in range(N):
            rst += MAP[i].count(0)

        if rst > maxx:
            maxx = rst
        return

    for i in range(idx, total):
        W[i] = 1
        dfs(wall + 1, i + 1)
        W[i] = 0




N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
total = 0
cnt = 0
rst = 0
maxx = 0

for i in range(N):
    total += MAP[i].count(0)

W = [0 for _ in range(total)]



dfs(0, 0)
print(maxx)

