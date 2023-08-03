N = int(input())

if N % 4 == 0:
    ans = N // 4
else: ans = N // 4 + 1

ans_long = ""

for i in range(ans):
    ans_long += "long "

print(ans_long + "int")