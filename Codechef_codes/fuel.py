a = int(input())
for i in range(a):
    a1, a2, a3, a4, a5 = map(int, input().split())
    b = a1 + a3
    c = a2 + a4
    for i in range(a5):
        b = b + a3
        c = c + a4
    if b < c:
        print("PETROL")
    elif b > c:
        print("DIESEL")
    else:
        print("SAME PRICE")
