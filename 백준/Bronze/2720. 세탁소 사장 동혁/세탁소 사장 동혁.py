import sys
input = sys.stdin.readline

for i in range(int(input())):
    dollar = [0, 0, 0, 0]
    change = int(input())
    while change != 0:
        if change >= 25:
            change -= 25
            dollar[0] += 1
        elif change >= 10:
            change -= 10
            dollar[1] += 1
        elif change >= 5:
            change -= 5
            dollar[2] += 1
        else:
            change -= 1
            dollar[3] += 1
    print(*dollar)