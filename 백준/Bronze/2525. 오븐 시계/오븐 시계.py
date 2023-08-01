A, B = map(int, input().split())
C = int(input())

if C < 60 :
    B += C
else :
    A += int(C / 60)
    B += C % 60

if B >= 60 :
    A += 1
    B -= 60
    
if A >= 24 :
    A -= 24

print(f"{A} {B}")