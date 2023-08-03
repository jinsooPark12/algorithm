x = int(input())

x_p = 0

for i in range(int(input())):
    a, b = map(int,input().split())
    x_p += a * b

if x == x_p:
    print("Yes")

else: print("No")