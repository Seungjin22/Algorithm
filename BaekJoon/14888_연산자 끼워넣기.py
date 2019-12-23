import sys
sys.stdin = open('14888_input.txt')

import collections
import copy


def Perm(d, rst):
    if len(rst) == len(ops) and rst not in temp:
        temp.append(rst)
        return
    for i in range(len(ops)):
        if not chk[i]:
            chk[i] = 1
            Perm(d + 1, rst + [ops[i]])
            chk[i] = 0


def Calc(t):
    while t:
        a = nnums.popleft()
        b = nnums.popleft()
        op = t.pop(0)
        if op == 0:
            nnums.appendleft(a + b)
        elif op == 1:
            nnums.appendleft(a - b)
        elif op == 2:
            nnums.appendleft(a * b)
        else:
            if a < 0:
                nnums.appendleft(- (abs(a) // b))
            else:
                nnums.appendleft(a // b)
        if len(nnums) == 1: break


N = int(input())
nums = collections.deque(map(int, input().split()))
op_nums = list(map(int, input().split()))
ops = []
temp = []
maxx = 0
mini = 987654321

for idx, n in enumerate(op_nums):
    if n > 0:
        for i in range(n):
            ops.append(idx)

chk = [0] * len(ops)
Perm(0, [])

for t in temp:
    nnums = copy.copy(nums)
    Calc(t)
    ans = nnums.popleft()
    if ans <= mini:
        mini = ans
    elif ans >= maxx:
        maxx = ans
        print(maxx)

print(maxx)
print(mini)
