a = int(input())
for i in range(a):
    a1, a2, a3 = map(int, input().split())
    b = a2 * 3 + (a1 - a2) * (-1)
    if b >= a3:
        print("PASS")
    else:
        print("FAIL")
