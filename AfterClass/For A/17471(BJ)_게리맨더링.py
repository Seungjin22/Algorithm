import sys
sys.stdin = open('17471_input.txt')

import collections

def pprint(arr):
    for i in range(len(arr)):
        print(arr[i])


def Div(n, k):
    if n == k:
        for i in range(n):
            if A[i]:
                print(list(range(1, N + 1))[i])
        print()

    else:
        A[k] = 1
        Div(n, k + 1)
        A[k] = 0
        Div(n, k + 1)


def BFS(v):
    visited[v] = 1
    Q.append(v)
    while Q:
        t = Q.popleft()
        for i in range(N):
            if area[t][i] == 1 and visited[i] == 0:
                Q.append(i)
                visited[i] = visited[t] + 1



N = int(input())
P = list(map(int, input().split()))
area = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for n in range(1, N + 1):
    temp = list(map(int, input().split()))
    T = temp.pop(0)
    for t in temp:
        area[n][t] = 1


pprint(area)
A = [0] * N
visited = [0] * (N + 1)
Q = collections.deque()
Div(N, 0)
