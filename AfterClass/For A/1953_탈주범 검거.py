import sys
sys.stdin = open('1953_input.txt')
"""
BFS는 Q를 잘이용하자!
-> 계속 변해야 하는 값들을 Q에 넣어서 데리고 다녀주기
-> 좌표값도 Q에 넣어서 옮겨줘야 이동이 가능

x, y 좌표로 볼 때 값 위치 헷갈리지 말기!! 행|렬 !!!
-> 상, 하, 좌, 우 헷갈렸음

마지막 값은 cnt로 셀 필요가 없음 -> visited에 찍힌 1들의 합이 곧 답ㄴ
"""
import collections

def BFS(C, R, L):
    visited[R][C] = 1
    Q.append([C, R, L, MAP[R][C], 99])
    while Q:
        C, R, L, t, tt = Q.popleft()
        if L == 0: return
        if tt == 0 and 1 not in tunnel[t]: continue
        if tt == 1 and 0 not in tunnel[t]: continue
        if tt == 2 and 3 not in tunnel[t]: continue
        if tt == 3 and 2 not in tunnel[t]: continue
        visited[R][C] = 1
        for idx in tunnel[t]:
            x = C + dx[idx]
            y = R + dy[idx]
            if x < 0 or x >= M or y < 0 or y >=N: continue
            if MAP[y][x] != 0 and visited[y][x] == 0:
                Q.append([x, y, L - 1, MAP[y][x], idx])

for tc in range(1, int(input()) + 1):
    # N: 지도 세로 크기, M: 가로 크기, R: 맨홀 위치 y, C: 맨홀 위치 x, L: 탈출 후 소요 시간
    N, M, R, C, L = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
       # 우,좌,하,상
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    tunnel = { 1: [0, 1, 2, 3], 2: [2, 3], 3: [0, 1], 4: [3, 0], 5: [2, 0], 6: [1, 2], 7: [1, 3]}
    Q = collections.deque()
    BFS(C, R, L)
    ans = 0
    for i in range(N):
        ans += visited[i].count(1)
    print('#{} {}'.format(tc, ans))