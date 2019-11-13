import sys
sys.stdin = open('4008_input.txt')

import collections

def Perm(d, rst):
    if len(rst) == len(opers):
        if rst not in ops:
            ops.append(rst)
        return
    for i in range(len(opers)):
        if not chk[i]:
            chk[i] = 1
            Perm(d + 1, rst + [opers[i]])
            chk[i] = 0

def Calc(nums, ops):
    cnt = 0
    aa = nums.popleft()
    fin[0] = aa
    while cnt != len(ops):
        if ops[cnt] == '+':
            fin[0] += nums[cnt]
        elif ops[cnt] == '-':
            fin[0] -= nums[cnt]
        elif ops[cnt] == '*':
            fin[0] = fin[0] * nums[cnt]
        else:
            fin[0] = int(fin[0] / nums[cnt])
        cnt += 1
    nums.appendleft(aa)


for tc in range(1, int(input()) + 1):
    N = int(input())
    ON = collections.deque(map(int, input().split()))
    nums = collections.deque(map(int, input().split()))
    opers = collections.deque()
    ops = collections.deque()
    rst = collections.deque()
    fin = [0]
    ffin = []
    idx = 0
    for i in ON:
        for _ in range(i):
            if idx == 0:
                opers.append('+')
            elif idx == 1:
                opers.append('-')
            elif idx == 2:
                opers.append('*')
            elif idx == 3:
                opers.append('/')
        idx += 1

    chk = [0] * len(opers)
    Perm(0, [])
    for op in ops:
        Calc(nums, op)
        ffin.append(fin[0])
    print('#{} {}'.format(tc, max(ffin) - min(ffin)))