a = int(input())
for i in range(a):
    a1, a2, a3 = map(int, input().split())
    if a1 + a2 < a3:
        print("PLANEBUS")
    elif a1 + a2 > a3:
        print("TRAIN")
    else:
        print("EQUAL")
