import sys

N, M = map(int,sys.stdin.readline().split())

A, B = [],[]
an, bn = [],[]
ans = []

for _ in range(N):
    an = sys.stdin.readline().split()
    an = [int(i) for i in an]
    if len(an) == M:
        A.append(an)

for _ in range(N):
    bn = sys.stdin.readline().split()
    bn = [int(i) for i in bn]
    if len(bn) == M:
        B.append(bn)

for i in range(N):
    for j in range(M):
        print(f"{A[i][j] + B[i][j]} ",end="")
    print("")