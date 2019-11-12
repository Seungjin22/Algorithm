N = 3 # 배열의 길이
A = [0 for _ in range(N)]
data = [1, 2, 3]

# def printSet(n):
#     for i in range(n):
#         if A[i] == 1:
#             print("%d " % data[i], end="")
#     print()

def powerset(n, k):
    if n == k:
        print(A)
        # printSet(n)
    else:
        A[k] = 1
        powerset(n, k + 1)
        A[k] = 0
        powerset(n, k + 1)

powerset(N, 0)