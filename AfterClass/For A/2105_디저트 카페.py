import sys
sys.stdin = open('2105_input.txt')

for tc in range(1, int(input()) + 1):
    N = int(input())
    Cafe = [list(map(int, input().split())) for _ in range(N)]

    for i in range(1, N - 1):
        for j in range(1, M - 1):
            for rd in range(N - i - 1):

            for ld in range(i):

