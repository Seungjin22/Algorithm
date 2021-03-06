import sys
sys.stdin = open('14888_input.txt')

def DFS(fin, i):
    global mini, maxx
    if i == len(nums):
        if fin > maxx:
            maxx = fin
        if fin < mini:
            mini = fin
        return
    for j in range(4):
        if ON[j]:
            if j == 0:
                temp = fin + nums[i]
            elif j == 1:
                temp = fin - nums[i]
            elif j == 2:
                temp = fin * nums[i]
            else:
                temp = int(fin / nums[i])
            ON[j] -= 1
            DFS(temp, i+1)
            ON[j] += 1


N = int(input())
nums = list(map(int, input().split()))
ON = list(map(int, input().split()))
mini = 987654321
maxx = -987654321

DFS(nums[0], 1)
print(maxx)
print(mini)