a = int(input())
for i in range(a):
    a1, a2, a3 = map(int, input().split())
    b1, b2, b3 = map(int, input().split())
    A1 = 0
    B1 = 0
    if a1 > b1:
        A1 += 1
    else:
        B1 += 1
    if a2 > b2:
        A1 += 1
    else:
        B1 += 1
    if a3 > b3:
        A1 += 1
    else:
        B1 += 1
    if A1 > B1:
        print("A")
    else:
        print("B")
