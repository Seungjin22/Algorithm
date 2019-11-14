import sys
sys.stdin = open('17472_input.txt')


def Counting(x, y):
    MMAP[x][y] = num
    for idx in range(4):
        a = x + dx[idx]
        b = y + dy[idx]
        if a < 0 or a >= N or b < 0 or b >= M: continue
        if MAP[a][b] != 0 and MMAP[a][b] == 0:
            Counting(a, b)

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
MMAP = [[0 for _ in range(M)] for _ in range(N)]

num = 1
for i in range(N):
    for j in range(M):
        if MAP[i][j] and MMAP[i][j] == 0:
            Counting(i, j)
            num += 1
for i in range(N):
    print(MMAP[i])

print(num)
visited = [0] * num

print(visited)

