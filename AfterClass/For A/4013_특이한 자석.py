import sys
sys.stdin = open('4013_input.txt')
"""
마지막까지 고려하지 못한 부분!
-> flag도 넘겨주며 해결
"""
import collections


def Match(M, D): # m: 회전시키려는 자석 번호, d: 회전방향

    Q.append([M, D, 0])
    while Q:
        m, d, flag = Q.popleft()
        # 오른쪽 확인
        if m < 4 and visited[m + 1] == 0 and d != 0:
                flag = 0
                # 만약 극이 같다면 (회전 X)
                if Ms.get(m)[2] == Ms.get(m + 1)[-2]:
                    nd = 0
                # 극이 다르다면 (반대 방향 회전)
                else:
                    nd = -d
                Q.append([m + 1, nd, flag])

        # 왼쪽 확인
        if m > 1 and visited[m - 1] == 0 and d != 0:
                flag = 1
                # 만약 극이 같다면 (회전 X)
                if Ms.get(m)[-2] == Ms.get(m - 1)[2]:
                    nd = 0
                # 극이 다르다면 (반대 방향 회전)
                else:
                    nd = -d
                Q.append([m - 1, nd, flag])

        Spin(m, d, flag)
        visited[m] = 1
        if visited == [1, 1, 1, 1, 1]: return


def Spin(m, d, flag):
    if d == 0:
        if flag == 0:
            for i in range(m + 1, 5):
                visited[i] = 1
        else:
            for i in range(1, m):
                visited[i] = 1
        return
    elif d == 1:
        Ms[m].appendleft(Ms[m].pop())
    elif d == -1:
        Ms[m].append(Ms[m].popleft())


for tc in range(1, int(input()) + 1):
    K = int(input())
    Ms = {}
    info = []
    for i in range(4):
        Ms[i + 1] = collections.deque(map(int, input().split()))

    for _ in range(K):
        info.append(list(map(int, input().split())))

    for i in info:
        Q = collections.deque()
        visited = [1] + [0] * 4
        M, D = i
        Match(M, D)

    score = 0
    for key in Ms.keys():
        if Ms[key][0]:
            score += 2 ** (key - 1)
    print('#{} {}'.format(tc, score))
