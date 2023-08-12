row_list = [input() for i in range(5)]
maximum = 0

for i in row_list:
    maximum = max(maximum, len(i))

for i in range(maximum):
    for j in range(5):
        if len(row_list[j])<=i:
            continue
        print(row_list[j][i],end="")