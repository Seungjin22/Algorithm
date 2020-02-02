import sys
sys.stdin = open('10844_input.txt')


def Stairs(rst):
    global cnt
    if rst[-1] == '0':
        cnt += 1
        return
    if rst[-1] == '9':
        cnt += 1
        return
    if len(rst) == N:
        cnt += 1
        return
    for i in range(1, 10):
        if i == 9:
            cnt += 1
            break
        a = i - 1
        b = i + 1
        if a == 10: a = 0
        if b == 10: b = 0
        Stairs(rst + str(i) + str(a))
        Stairs(rst + str(i) + str(b))

N = int(input())
cnt = 0

if N == 1:
    cnt = 9
else:
    Stairs('')

print(cnt)