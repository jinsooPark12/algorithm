import sys
input = sys.stdin.readline

for i in range(int(input())):
    dollar = [0, 0, 0, 0]
    change = int(input())
    
    dollar[0] = change // 25
    change %= 25
    dollar[1] = change // 10
    change %= 10
    dollar[2] = change // 5
    change %= 5
    dollar[3] = change
    
    print(*dollar)