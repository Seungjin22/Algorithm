import sys
sys.stdin = open('2636_input.txt')

def DFS(x, y):
    visited[x][y] = 1

    for idx in range(4):
        a = x + dx[idx]
        b = y + dy[idx]
        if a < 0 or a >= N or b < 0 or b >= M: continue
        if visited[a][b] != 0 and

N, M = map(int, input().split())
PAN = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
