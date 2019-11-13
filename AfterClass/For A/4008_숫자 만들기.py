import sys
sys.stdin = open('4008_input.txt')

import collections

def DFS(i):
    global fin, mini, maxx
    if i == len(case):
        Calc(nums, case)
        return
    for j in range(4):
        if case[i] == 0:
            if ON[j]:
                ON[j] -= 1
                if j == 0:
                    case[i] = 1
                elif j == 1:
                    case[i] = 2
                elif j == 2:
                    case[i] = 3
                else:
                    case[i] = 4
                DFS(i+1)
                case[i] = 0 # 초기화(클리어)
                ON[j] += 1


def Calc(nums, ops):
    global fin, mini, maxx
    cnt = 1
    fin = nums[0]
    while cnt != len(ops) + 1:
        if ops[cnt - 1] == 1:
            fin += nums[cnt]
        elif ops[cnt - 1] == 2:
            fin -= nums[cnt]
        elif ops[cnt - 1] == 3:
            fin = fin * nums[cnt]
        else:
            fin = int(fin / nums[cnt])
        cnt += 1
    if fin > maxx:
        maxx = fin
    if fin < mini:
        mini = fin

for tc in range(1, int(input()) + 1):
    N = int(input())
    ON = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    case = [0] * sum(ON)
    fin = 0
    mini = 987654321
    maxx = -987654321

    DFS(0)
    print('#{} {}'.format(tc, maxx - mini))