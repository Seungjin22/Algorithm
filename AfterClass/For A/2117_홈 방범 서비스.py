import sys
sys.stdin = open('2117_input.txt')

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    City = [list(map(int, input().split())) for _ in range(N)]