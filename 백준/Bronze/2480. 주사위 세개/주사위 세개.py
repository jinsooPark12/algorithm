dice = input().split()
dice = [int(i) for i in dice]

dice.sort(reverse = True)

for i in range(len(dice)) :
    if dice.count(dice[i]) == 3 :
        ans = 10000 + dice[i] * 1000
        break
    elif dice.count(dice[i]) == 2 :
        ans = 1000 + dice[i] * 100
        break
    else :
        ans = dice[0] * 100

print(ans)