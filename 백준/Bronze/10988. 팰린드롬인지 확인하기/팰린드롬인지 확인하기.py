a = input()
palindrome = 1

for i in range(len(a) // 2):
    palin1 = a[i]
    palin2 = a[len(a) - 1 - i]

    if palin1 != palin2:
        palindrome = 0
        break
print(palindrome)