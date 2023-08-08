S = input()

abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
       "n","o","p","q","r","s","t","u","v","w","x","y","z"]

for i in range(len(abc)):
    if abc[i] in S:
        abc[i] = S.index(abc[i])
    else:
        abc[i] = -1

for i in abc:
    print(f"{i} ",end = "")