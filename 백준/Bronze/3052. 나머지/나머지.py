import sys

num = []

for _ in range(10):
    num.append(int(sys.stdin.readline()) % 42)

num = sorted(num)

pn_li = []
pn = 0
for i in range(len(num)):
    if num.count(num[i]) == 1:
        pn += 1
        continue
    else:
        if num[i] in pn_li:
            continue
        else:
            pn_li.append(num[i])
            pn += 1
            continue
print(pn)