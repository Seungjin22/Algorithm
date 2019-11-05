import sys
sys.stdin = open('input.txt')

def Perm(d, rst):
    if len(rst) == M:
        for i in range(len(rst)):
            print(rst[i], end=" ")
        print()
        # print(' '.join(map(str, rst)))
        return
    for i in range(len(arr)):
        if not chk[i]:
            chk[i] = 1
            Perm(d + 1, rst + [arr[i]])
            chk[i] = 0


N, M = map(int, input().split())
arr = list(range(1, N+1))

chk = [0]*len(arr)

Perm(1, [])

