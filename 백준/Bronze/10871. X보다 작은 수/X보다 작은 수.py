import sys

N, X = map(int, sys.stdin.readline().split())

A = sys.stdin.readline().split()

A = [int(i) for i in A]

for i in range(len(A)):
    if X > A[i]:
        print(f"{A[i]} ", end = "")