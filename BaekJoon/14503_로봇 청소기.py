import sys
sys.stdin = open('14503_input.txt')
"""
후진했을 경우 뒤에 벽이라면 바로 정지!하는 조건 고려해주기
정지하는 조건문 flag로 세우기!
재귀 안의 재귀라 하나 빠져나와도 그 다음 재귀를 피하지 못했음...

nd = (d + 4 - i) % 4
-> Nyapy의 추천, 이렇게 방향에 따라 선택해보는건 어떨까?
"""


def Cleaning(r, c, d):
    global flag
    global rst
    global ans
    if d == 0:  # 북쪽을 바라볼때
        dy = [-1, 0, 1, 0]  # 서남동북
        dx = [0, 1, 0, -1]

    elif d == 1:  # 동쪽을 바라볼때
        dy = [0, -1, 0, 1]  # 북서남동
        dx = [-1, 0, 1, 0, ]

    elif d == 2:  # 남쪽을 바라볼때
        dy = [1, 0, -1, 0]  # 동북서남
        dx = [0, -1, 0, 1]

    elif d == 3:  # 서쪽을 바라볼때
        dy = [0, 1, 0, -1]  # 남동북서
        dx = [1, 0, -1, 0]

    if MAP[r][c] == 1: return
    if visited[r][c] == 0 and MAP[r][c] == 0:
        visited[r][c] = 1
        ans += 1
    cnt = 0
    for idx in range(4):
        x = r + dx[idx]
        y = c + dy[idx]
        if 0 <= x < N and 0 <= y < M and MAP[x][y] == 0 and visited[x][y] == 0:
            if dy[idx] == -1 and dx[idx] == 0: d = 3
            elif dy[idx] == 0 and dx[idx] == 1: d = 2
            elif dy[idx] == 1 and dx[idx] == 0: d = 1
            else: d = 0
            Cleaning(x, y, d)
            if flag == 1: return
        else:
            cnt += 1
            continue
    if cnt >= 3:
        a = r + dx[1]
        b = c + dy[1]
        if MAP[a][b] == 0:
            Cleaning(a, b, d)
        else:
            flag = 1
            return


N, M = map(int, input().split())
r, c, d = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
ans = 0
flag = 0

Cleaning(r, c, d)
print(ans)