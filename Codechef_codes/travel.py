a = int(input())
for i in range(a):
    a1, a2 = map(int, input().split())
    if a1 < a2:
        print("BIKE")
    elif a2 < a1:
        print("CAR")
    else:
        print("SAME")
