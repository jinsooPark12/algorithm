s = input()
n = 0

for i in s:
    if i == "A" or i == "B" or i == "C":
        n += 3
    elif i == "D" or i == "E" or i == "F":
        n += 4
    elif i == "G" or i == "H" or i == "I":
        n += 5
    elif i == "J" or i == "K" or i == "L":
        n += 6
    elif i == "M" or i == "N" or i == "O":
        n += 7
    elif i == "P" or i == "Q" or i == "R" or i == "S":
        n += 8
    elif i == "T" or i == "U" or i == "V":
        n += 9
    elif i == "W" or i == "X" or i == "Y" or i == "Z":
        n += 10

print(n)