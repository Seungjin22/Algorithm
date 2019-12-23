import sys
sys.stdin = open('14889_input.txt')

def Comb(d, start):
    global mini
    ta = 0
    tb = 0
    if len(start) == N // 2:
        link = []
        for m in men:
            if m not in start:
                link.append(m)

        for i in range(len(start)):
            for j in range(i + 1, len(start)):
                ta += data[start[i]][start[j]] + data[start[j]][start[i]]
                tb += data[link[i]][link[j]] + data[link[j]][link[i]]
        ans = abs(ta - tb)
        if ans < mini:
            mini = ans
        return
    for i in range(d, len(men)):
        Comb(i + 1, start + [men[i]])


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
men = []
link = []
cap = []
men = list(range(0, N))
mini = 987654321

Comb(0, [])

print(mini)