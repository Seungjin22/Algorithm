import sys
sys.stdin = open('1389_input.txt')


def Check(i, j):
    if i == j:
        pass


N, M = map(int, input().split())
R = list([0 for _ in range(N + 1)] for _ in range(N + 1))

for _ in range(M):
    x, y = map(int, input().split())
    R[x][y] = 1
    R[y][x] = 1

for i in range(1, N + 1):
    for j in range(1, N + 1):
