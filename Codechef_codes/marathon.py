a = int(input())
for i in range(a):
    a1, a2, a3, a4, a5 = map(int, input().split())
    b = a1 * a2
    if b < 10:
        print(0)
    elif b >= 10 and b < 21:
        print(a3)
    elif b >= 21 and b < 42:
        print(a4)
    else:
        print(a5)
