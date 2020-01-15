import sys
sys.stdin = open('1389_input.txt')
"""
BFS 교열이도 내 1 친구
DFS 교열이는 3 친구
"""

def Check(i, j):
    if i == j:
        pass


N, M = map(int, input().split())
R = list([0 for _ in range(N + 1)] for _ in range(N + 1))

for _ in range(M):
    x, y = map(int, input().split())
    R[x][y] = 1
    R[y][x] = 1

print(R)

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if R[i][j] == 1:
            Check(i, j)
            pass
