import sys
sys.stdin = open('2383_input.txt')


def Move(A):
    ta = 0
    tb = 0
    total = 0
    for i in range(len(A)):
        mx, my = men[i]
        # B 계단일때
        if A[i]:
            sx, sy = stairs[1]
            k = K[1]
            ss = abs(sx - mx) + abs(sy - my)
            aa.append(ss)
            aa.sort()
            a = 1
            while StairA[ss + a] == 3:
                a += 1
            for j in range(ss + a, ss + a + k + 1):
                if ta < ss + a + k:
                    ta = ss + a + k
                StairA[j] += 1

        # A 계단일때
        else:
            sx, sy = stairs[0]
            k = K[0]
            ss = abs(sx - mx) + abs(sy - my)
            bb.append(ss)
            bb.sort()
            b = 1
            while StairB[ss + b] == 3:
                b += 1
            for j in range(ss + b, ss + b + k + 1):
                if tb < ss + b + k:
                    tb = ss + b + k
                StairB[j] += 1

    total = max(ta, tb)
    return total

def powerset(n, k):
    global mini
    if n == k:
        rst = Move(A)
        if rst < mini:
            mini = rst
        return

    A[k] = 1
    powerset(n, k + 1)
    A[k] = 0
    powerset(n, k + 1)


for tc in range(1, int(input()) + 1):
    N = int(input())
    Room = [list(map(int, input().split())) for _ in range(N)]
    stairs = []
    men = []
    K = []
    mini = 987654321


    for i in range(N):
        for j in range(N):
            if Room[i][j] >= 2 and Room[i][j] <= 10:
                K.append(Room[i][j])
                stairs.append([i, j])
            if Room[i][j] == 1:
                men.append([i, j])

    A = [0 for _ in range(len(men))]
    StairA = [0] * 200
    StairB = [0] * 200
    aa = []
    bb = []

    N = len(men)
    powerset(N, 0)
    print("#{} {}".format(tc, mini))

