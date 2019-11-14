import sys
sys.stdin = open('17471_input.txt')
"""
부분집합으로 두 개의 선거구 나눠주기 (A, B)
BFS로 각 그룹 연결되었는지 확인
두 선거구로 나눌 수 없는 경우(-1 출력) 고려해주기!
-> flag = -1 전역에 두고 mini 갱신하는 경우가 아니라면 전부 예외 케이스 (-1)
-> flag 사용해서 flag가 -1인 경우 flag(-1) 출력, 아니면 mini 출력
"""
import collections

def Div(n, k):
    global mini, flag
    if n == k:
        A = []
        B = []
        for i in range(n):
            if temp[i]:
                A.append(i + 1)
            else:
                B.append(i + 1)
        if A == [] or B == []: return
        rstA = BFS(A)
        if rstA == -1: return
        rstB = BFS(B)
        if rstB == -1: return
        if abs(rstA - rstB) < mini:
            mini = abs(rstA - rstB)
            flag = 1
    else:
        temp[k] = 1
        Div(n, k + 1)
        temp[k] = 0
        Div(n, k + 1)


def BFS(G):
    total = 0
    visited = [0] * (N + 1)
    visited[G[0]] = 1
    Q.append(G[0])
    while Q:
        t = Q.popleft()
        for i in range(1, N + 1):
            if area[t][i] and visited[i] == 0:
                if i in G:
                    Q.append(i)
                    visited[i] = 1
    for g in G:
        if visited[g] == 0: return -1
        else:
            total += P[g - 1]
    return total


N = int(input())
P = list(map(int, input().split()))
area = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for n in range(1, N + 1):
    temp = list(map(int, input().split()))
    T = temp.pop(0)
    for t in temp:
        area[n][t] = 1
flag = -1
temp = [0] * N
Q = collections.deque()
mini = 987654321
Div(N, 0)
if flag == -1:
    print(flag)
else:
    print(mini)