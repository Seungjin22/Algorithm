import sys
sys.stdin = open('8979_input.txt')


data = []
N, K = map(int, input().split())
cnt = 0
for _ in range(N):
    data.append(list(map(int, input().split())))
print(data)
data.sort()

for d in data:
    if d[0] != K:
        if d[1] > data[K - 1][1]:
            cnt += 1
        elif d[1] == data[K - 1][1]:
            if d[2] > data[K - 1][2]:
                cnt += 1
            elif d[2] == data[K - 1][2]:
                if d[3] > data[K - 1][3]:
                    cnt += 1

print(cnt + 1)