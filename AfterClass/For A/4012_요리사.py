import sys
sys.stdin = open('4012_input.txt')
"""
조합의 개념이 2번 사용되는 문제
식재료 종류가 4개인 경우(2와 2)가 아닌 6개(3과 3) 이상일 때,
★ 시너지 계산을 위한 식재료 A, B 그룹내의 조합 고려도 필요!
-> 식재료 그룹별 조합은 이중 for문 사용했음 | 조합 함수 안 조합 함수 구현하다 헷갈려서 후퇴
"""

def Comb(d, A):
    global mini
    ta = 0
    tb = 0
    if len(A) == N // 2:
        B = []
        for i in n:
            if i  not in A:
                B.append(i)
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                ta += S[A[i]][A[j]] + S[A[j]][A[i]]
                tb += S[B[i]][B[j]] + S[B[j]][B[i]]
        rst = abs(ta - tb)
        if rst < mini:
            mini = rst
        return
    for i in range(d, len(n)):
        Comb(i+1, A + [n[i]])


for tc in range(1, int(input()) + 1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    n = list(range(0, N))
    mini = 20000

    Comb(0, [])
    print('#{} {}'.format(tc, mini))
