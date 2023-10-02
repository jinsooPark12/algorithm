ch = []
result = 0
for i in range(100):
    ch.append([0]*100)
N = int(input())
for j in range(N):
    a, b = map(int, input().split())
    for k in range(a-1, a+9):
        for m in range(b-1, b+9):
            ch[k][m] = 1
for n in range(100):
    result += ch[n].count(1)
print(result)