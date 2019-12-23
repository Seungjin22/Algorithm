import sys
sys.stdin = open('15686_input.txt')

def Comb(d, rst):
    if len(rst) == M:
        survived.append(rst)
        return
    for i in range(d, len(chicks)):
        Comb(i + 1, rst + [chicks[i]])


N, M = map(int, input().split())
City = [list(map(int, input().split())) for _ in range(N)]
chicks = []
homes = []
survived = []
mini = 987654321

for i in range(N):
    for j in range(N):
        if City[i][j] == 2:
            chicks.append((i, j))
        elif City[i][j] == 1:
            homes.append((i, j))

Comb(0, [])
print(survived)
print()
for ss in survived:
    print(ss)
    print()
    cd = 0
    ans = [987654321] * len(homes)
    for i, h in enumerate(homes):
        for s in ss:
            print(s)
            print()
            cd = abs(h[0] - s[0]) + abs(h[1] - s[1])
            if ans[i] > cd:
                ans[i] = cd
    if sum(ans) < mini:
        mini = sum(ans)

print(mini)