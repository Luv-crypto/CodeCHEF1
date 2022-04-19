a = int(input())
for i in range(a):
    a1, a2 = map(int, input().split())
    b = a1 / (a2 * a2)
    if b <= 18:
        print("1")
    elif b > 18 and b <= 24:
        print("2")
    elif b >= 25 and b <= 29:
        print("3")
    else:
        print("4")
