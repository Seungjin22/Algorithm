import sys
sys.stdin = open('18231_input.txt')


N, M = map(int, input().split())
CITY = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    CITY[i][j] = 1

K = int(input())
P = list(map(int, input().split()))

"""

Hi
"""
