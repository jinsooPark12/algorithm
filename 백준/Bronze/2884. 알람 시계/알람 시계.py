H, M = map(int, input().split())

ans_M = M - 45

if ans_M >= 0 :
    print(f"{H} {ans_M}")
elif ans_M < 0 and H != 0 :
    print(f"{H - 1} {60 + ans_M}")
else:
    print(f"23 {60 + ans_M}")