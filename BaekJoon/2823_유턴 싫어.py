import sys
sys.stdin = open('2823_input.txt')
"""
BFS나 DFS로 풀 필요가 없는 문제
1. 경계를 고려해주지 못한 점!
-> 범위 벗어난 부분에서도 cnt 증가시켜주기
2. 이중 for문에서 break는 한 반복문만 중단
-> flag 초기화의 위치와 break문 한 번 더 써주기!
"""


R, C = map(int, input().split())
MAP = [list(input()) for _ in range(R)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
flag = 0

for i in range(R):
    for j in range(C):
        if MAP[i][j] == '.':
            cnt = 0
            for idx in range(4):
                x = i + dx[idx]
                y = j + dy[idx]
                if x < 0 or x >= R or y < 0 or y >= C:
                    cnt += 1
                    continue
                if MAP[x][y] == 'X':
                    cnt += 1
            if cnt >= 3:
                flag = 1
                break
    if flag:
        break

print(flag)
