import sys
sys.stdin = open('1713_input.txt')

N = int(input())
V = int(input())
S = list(map(int, input().split()))
voted = [0 for _ in range(101)]
ans = []

for s in S:
    mini = 1001
    if voted[s]:
        voted[s] += 1
    else:
        ans.append(s)
        voted[s] = 1

    if len(ans) > N:
        for idx in range(0,len(ans) - 1):
            if voted[ans[idx]] < mini:
                mini = voted[ans[idx]]
                a = ans[idx]
        ans.remove(a)
        voted[a] = 0

for answer in sorted(ans):
    print(answer, end=" ")