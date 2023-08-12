import sys
input = sys.stdin.readline

n = int(input())

square = pow(2,n)
square += 1

print(pow(square, 2))