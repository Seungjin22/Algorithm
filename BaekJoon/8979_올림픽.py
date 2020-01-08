import sys
sys.stdin = open('8979_input.txt')


def Compare(d, temp):
    cnt = 0
    iidx = 0
    gmax = max(medal[d])
    for idx, m in enumerate(medal[d]):
        if m == gmax and visited[idx] == 0:
            cnt += 1
            temp.append(idx)
            iidx = idx
    if cnt == 1 and visited[iidx] == 0:
        rst.append(iidx)
        visited[iidx] = 1
        medal[1][iidx] = 0
        medal[2][iidx] = 0
        medal[3][iidx] = 0
    elif cnt > 1:
        





data = []
N, K = map(int, input().split())
medal = {1:[], 2:[], 3:[]}
rst = []
temp = []
visited = [0 for _ in range(N)]
for _ in range(N):
    # data.append(list(map(int, input().split())))
    c, g, s, b = map(int, input().split())
    medal[1].append(g)
    medal[2].append(s)
    medal[3].append(b)

print(data)
print(medal)
Gmax = 0
Smax = 0
Bmax = 0
Compare(1)
# for i in range(N):
#     if data[i][1] > Gmax:
#         Gmax = data[i][1]
