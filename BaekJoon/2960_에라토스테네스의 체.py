import sys
sys.stdin = open('2960_input.txt')
"""
소수 구하기 문제를 풀어보자!
에라토스테네스 체의 개념
+ 소수의 제곱근보다 작은 소수로 나누어지지 않는다면 소수
"""
N, K = map(int, input().split())
rst = []
cnt = 0
nums = list(range(2, N + 1))

while(cnt != K):
    P = nums[0]
    for n in nums:
        if n % P == 0:
            nums.remove(n)
            rst.append(n)
            cnt += 1
            if cnt == K: break

print(rst[K - 1])