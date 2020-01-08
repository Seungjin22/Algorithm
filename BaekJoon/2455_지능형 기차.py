import sys
sys.stdin = open('2455_input.txt')

maxx = 0
ans = 0
for _ in range(4):
    a, b = map(int, input().split())
    ans -= a
    ans += b
    if ans > maxx:
        maxx = ans

if maxx > 10000:
    maxx = 10000

print(maxx)