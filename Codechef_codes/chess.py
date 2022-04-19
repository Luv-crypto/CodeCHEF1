a = int(input())
for i in range(a):
    a1, a2 = map(int, input().split())
    if a1 + a2 < 3:
        print("1")
    elif a1 + a2 >= 3 and a1 + a2 <= 10:
        print("2")
    elif a1 + a2 >= 11 and a1 + a2 <= 60:
        print("3")
    else:
        print("4")
