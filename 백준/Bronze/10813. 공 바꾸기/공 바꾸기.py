import sys
input = sys.stdin.readline

N, M = map(int, input().split())
basket = [i for i in range(1, N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    ret = basket[a - 1]
    basket[a - 1] = basket[b - 1]
    basket[b - 1] = ret

print(*basket)